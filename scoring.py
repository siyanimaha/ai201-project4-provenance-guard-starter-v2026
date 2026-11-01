"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here.

`combine_signals` combines the model and style signals into one score.

`score_to_label` turns that score into something a person can understand.

The README's Signals and Scoring section should name:
`scoring.py::combine_signals`
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score.

    Both inputs use higher scores to mean more likely AI.
    The two signals are weighted using the values in config.py.
    """
    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )

    return round(max(0.0, min(combined, 1.0)), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn the combined score into a machine-readable guess
    and reader-friendly label.
    """

    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "This writing shows patterns that are more consistent with "
            "AI-generated text, but this result is not proof of authorship.",
        )

    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "This writing shows patterns that are more consistent with "
            "human-written text.",
        )

    return (
        "unsure",
        "We are not confident whether this writing was produced by a person or AI.",
    )


def label_ranges() -> list[tuple[str, str]]:
    """
    Return the score range covered by each label.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]