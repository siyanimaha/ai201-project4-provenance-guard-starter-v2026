
# Provenance Guard

**CodePath AI201 — Applications of AI Engineering**

## Getting Started

Provenance Guard is a Flask web service that analyzes writing and estimates whether it shows patterns associated with AI-generated or human-written text.

Start the application:

    python app.py

The service runs at `http://127.0.0.1:5000`.

For setup instructions, see [RUNNING.md](RUNNING.md).

---

# Unit 7 — The Build

## What This Does

1. A writer submits text and a creator ID to `/submit`.
2. `detector.py::model_signal` analyzes text predictability using GPT-2.
3. `stylometry.py::style_signal` analyzes writing patterns.
4. `scoring.py::combine_signals` combines both scores.
5. `scoring.py::score_to_label` assigns a classification.
6. `audit.py` records the decision.
7. The API returns the result and an explanation.

The system provides an estimate, not proof of authorship.

## Signals and Scoring

### Signal One — Model Signal

**What it measures:**

The model signal uses GPT-2 perplexity to measure how predictable submitted writing is.

Higher scores indicate writing that appears more AI-like according to this signal.

**Why it matters:**

AI-generated writing can contain predictable language patterns.

**Limitations:**

Human writing can also be predictable, particularly when it is simple or formal. Edited AI writing may be less predictable.

Predictability alone cannot prove authorship.

### Signal Two — Style Signal

**What it measures:**

The style signal analyzes:

- Sentence-length variation
- Vocabulary variety
- Punctuation density

**Why it matters:**

AI-generated writing may use consistent sentence structures and vocabulary patterns.

**Limitations:**

Human writers can also write consistently, and AI-generated text can imitate human variation.

These patterns do not reliably prove who wrote the text.

### The Combining Rule

The system combines both signals using equal weights.

**Model weight:** 0.50

**Style weight:** 0.50

Formula:

    combined_score = (0.50 * model_score) + (0.50 * style_score)

Implementation: `scoring.py::combine_signals`

**Example where the signals disagreed:**

| Signal | Score |
|---|---:|
| Model | 0.6722 |
| Style | 0.4904 |
| Combined | 0.5813 |

The combined score resulted in an unsure classification.

This demonstrates why combining signals can be useful when individual measurements disagree.

---

## Label Variants

| Label | Score range |
|---|---|
| Human | 0.00–0.35 |
| Unsure | Above 0.35 and below 0.65 |
| AI | 0.65–1.00 |

**Human message:**

"This writing shows patterns that are more consistent with human-written text."

**Unsure message:**

"We are not confident whether this writing was produced by a person or AI."

**AI message:**

"This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship."

I chose these messages because the system should communicate uncertainty instead of accusing writers of using AI.

Earlier manual testing produced all three labels:

| Label | Score |
|---|---:|
| Human | 0.3005 |
| Unsure | 0.5813 |
| AI | 0.7109 |

The later Unit 8 evaluation scenarios did not reproduce the human label.

---

## Sample Run

### A Submission

Command:

    curl -X POST http://127.0.0.1:5000/submit \
      -H "Content-Type: application/json" \
      -d '{"text":"The system works well. It handles most cases correctly and provides good results. Users generally find it easy to use and understand.","creator_id":"siyani"}'

**Recorded response:**

    {
      "confidence": 0.5813,
      "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
      "guess": "unsure",
      "label": "We are not confident whether this writing was produced by a person or AI.",
      "model_score": 0.6722,
      "style_score": 0.4904
    }

### An Appeal

Command:

    curl -X POST http://127.0.0.1:5000/appeal \
      -H "Content-Type: application/json" \
      -d '{"content_id":"e7db2c2c-3b27-479b-ad20-b31bd4129a81","reasoning":"I wrote this text myself and would like the result reviewed."}'

**Recorded response:**

    {
      "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
      "message": "Your appeal has been recorded and is under review.",
      "status": "under_review"
    }

The appeal workflow allows a writer to request a review instead of treating the initial classification as final.

---

## How I Used AI

### Moment 1 — Debugging the API

**What I asked for:**

I asked AI to help debug my Flask `/submit` endpoint because the style score was returning `null`.

**What came back:**

AI helped identify issues with connecting the scoring functions and saving changes to the application.

**What I changed:**

I corrected the implementation and tested the endpoint until both scores appeared in the response.

### Moment 2 — Classification and Appeals

**What I asked for:**

I asked AI for help implementing the three classification labels and the appeal workflow.

**What came back:**

AI provided code suggestions and example requests.

**What I changed:**

I tested the API responses and improved the handling of invalid requests.

### Moment 3 — Unit 8 Testing

**What I asked for:**

I asked AI to help prepare evaluation scenarios, interpret attack results, and organize the README.

**What came back:**

AI generated synthetic human-style examples, comparison examples, and explanations of the test results.

**What I changed:**

I executed the tests, examined the outputs, and documented the weaknesses.

The synthetic human-style examples were generated by AI and are not evidence of performance on genuinely human-written text.

---

# Unit 8 — The Test

## Rate Limiting

I implemented rate limiting to prevent users from overwhelming the submission endpoint.

The configured limits are:

- 10 submissions per minute
- 200 submissions per day

These limits allow normal use while restricting excessive repeated requests.

### Rate-Limit Test

Command:

    python run_attacks.py --flood 15

**Observed results:**

| Response | Requests |
|---|---:|
| HTTP 200 | 10 |
| HTTP 429 | 5 |
| Total | 15 |

The first ten requests succeeded.

The remaining five requests were rejected with HTTP 429.

An earlier audit-log inspection showed 24 entries, including five rate-limit rejections.

The limiter currently uses in-memory storage.

In production, I would use shared persistent storage so limits remain consistent across server restarts and multiple instances.

---

## Attack Run — Before

**Source:** `results/attack_run_2026-11-09_1809_before.md`

I ran the attack suite to identify weaknesses in the application.

The tests included evasion, false positives, prompt injection, malformed content, malformed requests, and flooding.

### Important Before-Run Findings

| Attack | Input | HTTP status | Verdict |
|---|---|---:|---|
| RQ04 | Malformed request | 400 | HELD |
| RQ05 | Null text | 400 | HELD |
| RQ06 | Creator ID is an object | 200 | BROKE |
| RQ07 | JSON array instead of object | 500 | BROKE |
| RQ08 | Unparseable JSON | 400 | HELD |
| RQ09 | Empty body | 400 | HELD |
| RQ10 | Form-encoded body | 400 | HELD |
| RQ11 | Incorrect content type | 400 | HELD |
| RQ12 | Deeply nested JSON | 400 | HELD |
| FL01_01–FL01_10 | First ten flood requests | 200 | HELD |
| FL01_11–FL01_12 | Excess flood requests | 429 | HELD |

The full original before-run report contains additional attack cases. Their individual outcomes are not reproduced in this table.

### RQ06 — Invalid Creator ID

The attack submitted a JSON object instead of a string as the creator ID.

The application accepted the request and returned HTTP 200.

It classified the submitted text as human.

**Verdict: BROKE**

The failure occurred during input validation because the application did not reject an invalid creator ID type.

### RQ07 — JSON Array Request

The attack submitted a JSON array instead of a JSON object.

The application attempted to call `.get()` on a list.

This caused an `AttributeError` and an HTTP 500 server error.

**Verdict: BROKE**

The failure occurred before classification because the request structure was not validated.

This was the most serious API reliability problem found in the confirmed before-run results.

### Flooding

The first ten requests returned HTTP 200.

Requests eleven and twelve returned HTTP 429.

**Verdict: HELD**

The rate limiter prevented the extra requests from being processed.

---

## Audit Logging

The application records submission decisions, rejected requests, and appeal events.

The log helps explain how the system arrived at a decision and provides information for investigating problems.

### Ten Audit Log Entries

The following examples include eight classification decisions, one rate-limit rejection, and one appeal.

The first nine are abbreviated records previously extracted from the audit data. The tenth is a complete appeal record confirmed directly from `logs/audit.jsonl`.

    [
      {
        "content_id": "d37193f0-2772-4fd3-80e9-e3de4dc3d0c2",
        "creator_id": "attacker_FP02",
        "guess": "ai",
        "model_score": 0.7387,
        "style_score": 0.6271,
        "combined_score": 0.6829,
        "status": "decided",
        "timestamp": "2026-11-09T23:21:37+00:00"
      },
      {
        "content_id": "26a75341-ac49-4bfa-a344-fe01e8c9b04e",
        "creator_id": "attacker_FP03",
        "guess": "ai",
        "model_score": 0.8051,
        "style_score": 0.594,
        "combined_score": 0.6996,
        "status": "decided",
        "timestamp": "2026-11-09T23:21:37+00:00"
      },
      {
        "content_id": "f57832fd-6fbc-44bd-a2f6-301ba91684d5",
        "creator_id": "attacker_FP04",
        "guess": "ai",
        "model_score": 0.8329,
        "style_score": 0.5405,
        "combined_score": 0.6867,
        "status": "decided",
        "timestamp": "2026-11-09T23:21:37+00:00"
      },
      {
        "content_id": "56375ba6-4390-49c8-aa92-15ad3222fe5d",
        "creator_id": "attacker_EV01",
        "guess": "unsure",
        "model_score": 0.1635,
        "style_score": 0.6006,
        "combined_score": 0.3821,
        "status": "decided",
        "timestamp": "2026-11-09T23:21:36+00:00"
      },
      {
        "content_id": "d63d636d-24c9-40ad-bdd4-53ddf607e367",
        "creator_id": "attacker_EV10",
        "guess": "ai",
        "model_score": 0.9792,
        "style_score": 0.7435,
        "combined_score": 0.8614,
        "status": "decided",
        "timestamp": "2026-11-09T23:21:37+00:00"
      },
      {
        "content_id": "5ca30375-3b45-4167-8074-1d06867fa448",
        "creator_id": "attacker_PI02",
        "guess": "human",
        "model_score": 0.2044,
        "style_score": 0.3815,
        "combined_score": 0.2929,
        "status": "decided",
        "timestamp": "2026-11-09T23:19:24+00:00"
      },
      {
        "content_id": "714f3cf7-4a58-4beb-91c8-f7441c274ee8",
        "creator_id": "attacker_MF03",
        "guess": "human",
        "model_score": 0.0,
        "style_score": 0.6667,
        "combined_score": 0.3333,
        "status": "decided",
        "timestamp": "2026-11-09T23:19:25+00:00"
      },
      {
        "content_id": "a76107c2-9769-467b-9c6d-c6f166d0d74c",
        "creator_id": "attacker_flood",
        "guess": "human",
        "model_score": 0.0287,
        "style_score": 0.606,
        "combined_score": 0.3173,
        "status": "decided",
        "timestamp": "2026-11-09T23:19:26+00:00"
      },
      {
        "creator_id": "attacker_flood",
        "event": "rejected",
        "limit": "10 per 1 minute",
        "reason": "rate_limited",
        "status": "rejected",
        "timestamp": "2026-11-09T23:19:26+00:00"
      },
      {
        "timestamp": "2026-11-09T23:56:11+00:00",
        "content_id": "f556c003-65c1-42d2-82ce-79ba4c6fb53c",
        "creator_id": "appeal_test_4",
        "event": "appeal",
        "status": "under_review",
        "reasoning": ""
      }
    ]

The original log should be used when complete unabridged audit records are required.

### The Single Worst Outcome

The most concerning classification problem was the false-positive behavior.

In the after-run, six of eight false-positive probes received AI classifications.

This is concerning because predictable human writing could be incorrectly classified as AI-generated.

An incorrect classification could unfairly affect a writer if someone treated the detector's output as proof.

---

## Run Log and Verdicts

I ran three evaluation commands:

    python run_eval.py --label before
    python run_eval.py --label trial2
    python run_eval.py --label trial3

The results were saved in:

- `results/run_2026-11-09_1851_before.md`
- `results/run_2026-11-09_1851_trial2.md`
- `results/run_2026-11-09_1851_trial3.md`

Each command ran three internal trials.

### Evaluation Results

| Criterion | Target | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| False positives | At most 1/10 genuine human texts classified AI | 10/10 synthetic samples classified AI | 10/10 | 10/10 |
| Score separation | AI mean at least 0.20 higher | Numerical verification pending | Pending | Pending |
| Label coverage | All three labels | AI and unsure | AI and unsure | AI and unsure |
| Appeals | 5/5 accepted and audited | 5/5 responses succeeded in separate test | Not repeated | Not repeated |
| Bad inputs | Controlled responses without crashes | No crash observed | No crash observed | No crash observed |

### Criterion 1 — False Positives

All ten synthetic human-style samples received AI classifications.

One example returned:

    {
      "status": 200,
      "guess": "ai",
      "confidence": 0.735,
      "model_score": 0.9011,
      "style_score": 0.5689
    }

The synthetic samples were AI-generated, so this test does not establish the false-positive rate for genuine human writing.

**Verdict:** The synthetic test performed poorly, but the genuine-human criterion remains unverified.

### Criterion 2 — Score Separation

Four of five AI examples received unsure classifications.

One received an AI classification.

This indicates that the detector was not consistently confident when evaluating those examples.

However, the required comparison concerns mean scores rather than classification counts.

**Verdict:** Numerical score separation still requires verification.

### Criterion 3 — Label Coverage

The evaluation produced AI and unsure labels.

It did not produce a human label.

Although earlier manual testing produced all three labels, these evaluation scenarios did not.

**Verdict: FAILED for the selected evaluation inputs.**

### Criterion 4 — Appeals

I submitted five separate pieces of writing and appealed their content IDs.

All five appeal requests returned HTTP 200 and `under_review`.

| Appeal | HTTP status | Result |
|---|---:|---|
| 1 | 200 | under_review |
| 2 | 200 | under_review |
| 3 | 200 | under_review |
| 4 | 200 | under_review |
| 5 | 200 | under_review |

One corresponding audit entry was confirmed:

    {
      "timestamp": "2026-11-09T23:56:11+00:00",
      "content_id": "f556c003-65c1-42d2-82ce-79ba4c6fb53c",
      "creator_id": "appeal_test_4",
      "event": "appeal",
      "status": "under_review",
      "reasoning": ""
    }

**Verdict:** All five API responses passed. Verification of all five audit entries is still pending.

### Criterion 5 — Bad Inputs

Missing and empty text were rejected without an observed crash.

An extremely long text input was accepted and classified as AI.

The endpoint handled these test inputs without an observed server failure.

**Verdict:** No crash observed; complete HTTP-status verification and stronger length validation remain possible improvements.

---

## Attack Diagnoses

### False-Positive Attacks

Six false-positive probes were classified as AI.

The model signal can assign high scores to predictable writing even when predictability is not proof of AI authorship.

The combining rule can then produce a score above the AI threshold.

**Failure stage:** Model signal and score combination.

### Evasion Attacks

Nine of ten evasion probes returned unsure.

Changes to sentence structure, vocabulary, and writing style can affect perplexity and stylometric measurements.

This can reduce the detector's confidence even when writing originated from AI.

**Failure stage:** Signal reliability and score calibration.

### Prompt-Injection Attacks

The prompt-injection probes produced human or unsure classifications.

These results alone do not prove that injected instructions changed the detector's behavior.

The service should continue treating submitted writing as data, not instructions.

**Risk area:** Input handling and detector robustness.

### Malformed Content

Some unusual content was rejected, while other inputs were accepted and classified.

The application could benefit from stricter validation of extreme or unusual text.

**Risk area:** Input validation.

### Malformed Requests

Before the improvement, RQ06 accepted an invalid creator ID and RQ07 caused an HTTP 500 error.

These problems occurred because the endpoint did not sufficiently validate the incoming JSON structure and field types.

**Failure stage:** Request validation.

### Flooding

The first ten requests were accepted.

Later requests returned HTTP 429.

**Verdict: HELD**

The configured rate limit successfully restricted excessive submissions.

---

## The Improvement

### What I Changed

I strengthened request validation in the submission endpoint.

The application now rejects JSON arrays where an object is required and rejects creator IDs with invalid data types.

I also implemented rate limiting to control excessive submissions.

### Why I Made This Change

The before-run showed two confirmed request-validation failures.

RQ06 accepted a creator ID with the wrong type.

RQ07 crashed when the request body was a JSON array.

These failures showed that the application needed to validate incoming requests before processing them.

### Before and After Comparison

| Attack | Before | After | Result |
|---|---|---|---|
| RQ06 — Creator ID is an object | HTTP 200 | HTTP 400 | Fixed |
| RQ07 — JSON array instead of object | HTTP 500 | HTTP 400 | Fixed |

### RQ06 — Before and After

**Before:**

The application accepted an object as the creator ID and returned HTTP 200.

**After:**

The application rejected the invalid creator ID and returned HTTP 400.

**Verdict: BROKE → HELD**

### RQ07 — Before and After

**Before:**

The application attempted to call `.get()` on a list.

This caused an HTTP 500 server error.

**After:**

The application rejected the JSON array with HTTP 400.

**Verdict: BROKE → HELD**

### Did the Improvement Work?

Yes, for the two confirmed request-validation vulnerabilities.

Both attacks changed from failures to controlled HTTP 400 responses.

The improvement made the API more reliable and prevented the previously observed crash.

However, it did not solve the detector's classification accuracy problems.

---

## Attack Run — After

**Source:** `results/attack_run_2026-11-09_1838_after.md`

I ran the attack suite again after making the changes.

The after-run contained 56 requests.

No HTTP 500 errors were observed.

### After-Run Summary

| Category | Observed results |
|---|---|
| Evasion EV01–EV10 | 9 unsure, 1 AI |
| False positives FP01–FP08 | 6 AI, 1 unsure, 1 human |
| Prompt injection PI01–PI06 | 5 unsure, 1 human |
| Malformed content MF01–MF08 | 2 HTTP 400, 6 HTTP 200 |
| Malformed requests RQ01–RQ12 | 11 HTTP 400, 1 HTTP 200 |
| Flood FL01_01–FL01_12 | 10 HTTP 200, 2 HTTP 429 |

### Detailed After-Run Results

The following table records the observed results. HELD and BROKE are manual interpretations based on the attack's purpose. For prompt-injection probes, the classification alone does not establish whether the injection succeeded.

| Attack | HTTP status | Classification | Assessment |
|---|---:|---|---|
| EV01 | 200 | unsure | Evasion concern |
| EV02 | 200 | unsure | Evasion concern |
| EV03 | 200 | unsure | Evasion concern |
| EV04 | 200 | unsure | Evasion concern |
| EV05 | 200 | unsure | Evasion concern |
| EV06 | 200 | unsure | Evasion concern |
| EV07 | 200 | unsure | Evasion concern |
| EV08 | 200 | unsure | Evasion concern |
| EV09 | 200 | unsure | Evasion concern |
| EV10 | 200 | AI | HELD |
| FP01 | 200 | unsure | Uncertain classification |
| FP02 | 200 | AI | False-positive concern |
| FP03 | 200 | AI | False-positive concern |
| FP04 | 200 | AI | False-positive concern |
| FP05 | 200 | AI | False-positive concern |
| FP06 | 200 | AI | False-positive concern |
| FP07 | 200 | AI | False-positive concern |
| FP08 | 200 | human | HELD |
| PI01 | 200 | unsure | Injection outcome unverified |
| PI02 | 200 | human | Injection outcome unverified |
| PI03 | 200 | unsure | Injection outcome unverified |
| PI04 | 200 | unsure | Injection outcome unverified |
| PI05 | 200 | unsure | Injection outcome unverified |
| PI06 | 200 | unsure | Injection outcome unverified |
| MF01 | 400 | None | HELD |
| MF02 | 400 | None | HELD |
| MF03 | 200 | human | Accepted unusual content |
| MF04 | 200 | human | Accepted unusual content |
| MF05 | 200 | AI | Accepted unusual content |
| MF06 | 200 | AI | Accepted unusual content |
| MF07 | 200 | AI | Accepted unusual content |
| MF08 | 200 | AI | Accepted unusual content |
| RQ01 | 400 | None | HELD |
| RQ02 | 200 | unsure | Missing creator ID accepted |
| RQ03 | 400 | None | HELD |
| RQ04 | 400 | None | HELD |
| RQ05 | 400 | None | HELD |
| RQ06 | 400 | None | HELD |
| RQ07 | 400 | None | HELD |
| RQ08 | 400 | None | HELD |
| RQ09 | 400 | None | HELD |
| RQ10 | 400 | None | HELD |
| RQ11 | 400 | None | HELD |
| RQ12 | 400 | None | HELD |
| FL01_01 | 200 | human | Allowed |
| FL01_02 | 200 | human | Allowed |
| FL01_03 | 200 | human | Allowed |
| FL01_04 | 200 | human | Allowed |
| FL01_05 | 200 | human | Allowed |
| FL01_06 | 200 | human | Allowed |
| FL01_07 | 200 | human | Allowed |
| FL01_08 | 200 | human | Allowed |
| FL01_09 | 200 | human | Allowed |
| FL01_10 | 200 | human | Allowed |
| FL01_11 | 429 | None | HELD |
| FL01_12 | 429 | None | HELD |

### What Improved?

RQ06 and RQ07 were fixed.

The application rejected invalid request structures with HTTP 400 instead of accepting them or crashing.

The after-run also produced no HTTP 500 errors.

### What Did Not Improve?

False-positive behavior remained a concern.

Six false-positive probes were still classified as AI.

Most evasion probes returned unsure.

The changes improved API reliability but did not establish better classification accuracy.

---

## What's Still Broken

### False Positives

Predictable writing can receive a high AI score even when predictability does not prove AI authorship.

The detector should be evaluated on genuinely human-written samples before being used in decisions affecting writers.

### Evasion

Modified AI-generated writing can receive unsure classifications.

The current signals are sensitive to changes in writing patterns.

### Label Coverage

The selected Unit 8 evaluation inputs did not produce all three classification labels.

The evaluation should include additional inputs that exercise the human classification range.

### Score Separation

The required numerical comparison of average AI and comparison-sample scores has not been verified.

### Appeal Auditing

Five appeal requests succeeded, and one audit record was directly confirmed.

The remaining four corresponding records should be checked.

### Input Validation

Some unusual content and extremely long submissions can still be accepted.

The service could benefit from clearer input-length limits and stricter validation.

### What I Would Improve Next

I would collect genuine human-written examples and verified AI-generated examples.

I would use those samples to measure false positives and calibrate the score thresholds.

I would also improve input-length validation and audit-log verification.

### The Trade I Would Make in Production

I would rather classify uncertain writing as unsure than incorrectly accuse a human writer of using AI.

This approach may allow some AI-generated writing to avoid confident detection, but it reduces the risk of unfair accusations.

The detector should support human review rather than serve as the final authority on authorship.

---

## Submission Checklist

### Unit 7

- [x] Five acceptance criteria defined in `criteria.md`
- [x] Submission endpoint implemented
- [x] Two scoring signals implemented
- [x] Three classification labels implemented
- [x] Appeal endpoint implemented
- [x] Combining rule documented
- [x] Sample submission and appeal included
- [ ] Verify required commit count

### Unit 8

- [x] Rate limiting implemented
- [x] HTTP 429 responses observed
- [x] Audit logging implemented
- [x] Attack suite executed
- [x] Confirmed before-run failures documented
- [x] After-run outcomes summarized individually
- [x] Ten audit-log examples included
- [x] Three evaluation commands completed
- [x] Evaluation weaknesses documented
- [x] Request-validation improvement implemented
- [x] RQ06 and RQ07 fixes verified
- [x] Remaining limitations documented
- [x] Production tradeoff explained
- [ ] Verify all five appeal audit entries
- [ ] Calculate mean-score separation
- [ ] Verify required commit count
- [ ] Add full unabridged audit records if required

---

## Repository

GitHub:

https://github.com/siyanimaha/ai201-project4-provenance-guard-starter-v2026

**How to run the project:** [RUNNING.md](RUNNING.md)
