
#!/usr/bin/env python3
"""
Provenance Guard — CodePath AI201 Project 4
Flask web service.
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config
import detector
import scoring
import stylometry


app = Flask(__name__)


# ==========================================
# JSON VALIDATION
# ==========================================

def get_payload():
    """
    Return a JSON dictionary or None.

    Reject JSON arrays, strings, numbers,
    null, and malformed JSON.
    """
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return None

    return payload


def invalid_request():
    return jsonify({
        "error": "invalid_request",
        "message": "Request body must be a JSON object."
    }), 400


# ==========================================
# RATE LIMITING
# ==========================================

class _LimiterOff:
    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()


if config.RATE_LIMITING_ENABLED:

    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        payload = get_payload()

        if payload is None:
            return get_remote_address()

        creator_id = payload.get("creator_id")

        if isinstance(creator_id, str):
            if creator_id.strip():
                return creator_id

        return get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        payload = get_payload() or {}

        creator_id = payload.get(
            "creator_id",
            "unknown"
        )

        if not isinstance(creator_id, str):
            creator_id = "unknown"

        audit.log_rejection(
            creator_id=creator_id,
            reason="rate_limited",
            limit=str(exc.description),
        )

        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ==========================================
# PING
# ==========================================

@app.post("/ping")
def ping():
    payload = get_payload()

    if payload is None:
        return invalid_request()

    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    }), 200


# ==========================================
# HEALTH
# ==========================================

@app.get("/health")
def health():
    loaded = detector._model is not None

    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    }), 200


# ==========================================
# SUBMIT
# ==========================================

@app.post("/submit")
@limiter.limit(
    f"{config.RATE_LIMIT_PER_MINUTE}/minute;"
    f"{config.RATE_LIMIT_PER_DAY}/day"
)
def submit():
    """
    Accept text, run detection signals,
    combine scores, log results, and
    return a prediction.
    """

    # FIX FOR RQ07:
    # Reject JSON arrays before using .get().
    payload = get_payload()

    if payload is None:
        return invalid_request()

    text = payload.get("text", "")

    creator_id = payload.get(
        "creator_id",
        "unknown"
    )

    # Validate text type.
    if not isinstance(text, str):
        return jsonify({
            "error": "invalid_text",
            "message": "Text must be a string."
        }), 400

    # Reject empty text.
    if not text.strip():
        return jsonify({
            "error": "invalid_text",
            "message": "Text is required and cannot be empty."
        }), 400

    # Validate creator ID.
    if not isinstance(creator_id, str):
        return jsonify({
            "error": "invalid_creator_id",
            "message": "Creator ID must be a string."
        }), 400

    if not creator_id.strip():
        return jsonify({
            "error": "invalid_creator_id",
            "message": "Creator ID cannot be empty."
        }), 400

    # Create a unique content ID.
    content_id = str(uuid.uuid4())

    # FIX FOR MF02:
    # Handle text too short for the detector.
    try:
        model_score = detector.model_signal(text)

    except ValueError as exc:
        return jsonify({
            "error": "invalid_text",
            "message": str(exc),
        }), 400

    # Calculate writing-style signal.
    style_score = stylometry.style_signal(text)

    # Combine the two signals.
    combined_score = scoring.combine_signals(
        model_score,
        style_score
    )

    # Generate prediction.
    guess, label = scoring.score_to_label(
        combined_score
    )

    # Record decision in audit log.
    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        label=label,
    )

    # Return prediction.
    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": combined_score,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
    }), 200


# ==========================================
# APPEAL
# ==========================================

@app.post("/appeal")
def appeal():
    payload = get_payload()

    if payload is None:
        return invalid_request()

    content_id = payload.get(
        "content_id",
        ""
    )

    reasoning = payload.get(
        "reasoning",
        ""
    )

    if not isinstance(content_id, str):
        return jsonify({
            "error": "invalid_content_id",
            "message": "Content ID must be a string."
        }), 400

    if not content_id.strip():
        return jsonify({
            "error": "invalid_content_id",
            "message": "Content ID is required."
        }), 400

    if not isinstance(reasoning, str):
        return jsonify({
            "error": "invalid_reasoning",
            "message": "Reasoning must be a string."
        }), 400

    entries = audit.entries_for(content_id)

    if not entries:
        return jsonify({
            "error": "not_found",
            "message": "No submission was found with that content ID.",
        }), 404

    creator_id = entries[0].get(
        "creator_id",
        "unknown"
    )

    audit.log_appeal(
        content_id=content_id,
        creator_id=creator_id,
        reasoning=reasoning,
    )

    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal has been recorded and is under review.",
    }), 200


# ==========================================
# AUDIT LOG
# ==========================================

@app.get("/log")
def get_log():
    limit = request.args.get(
        "limit",
        type=int
    )

    entries = audit.read_entries(
        limit=limit
    )

    return jsonify({
        "count": len(entries),
        "entries": entries,
    }), 200


# ==========================================
# START FLASK SERVER
# ==========================================

def main():
    print(
        f"Provenance Guard on "
        f"http://{config.HOST}:{config.PORT}"
    )

    print(
        f"  detector model: "
        f"{config.DETECTOR_MODEL}"
    )

    print(
        f"  rate limiting: "
        f"{'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}"
    )

    print(
        f"  audit log: "
        f"{config.AUDIT_LOG}"
    )

    print()
    print("Check it's alive:")

    print(
        f'  curl -X POST '
        f'http://{config.HOST}:{config.PORT}/ping \\'
    )

    print(
        '    -H "Content-Type: application/json" \\'
    )

    print(
        '    -d \'{"message": "hello"}\''
    )

    print()

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )


if __name__ == "__main__":
    main()
