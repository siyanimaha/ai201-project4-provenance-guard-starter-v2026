
# Provenance Guard

**CodePath AI201 — Applications of AI Engineering**

## Getting Started

This project is a Flask web service that analyzes writing and estimates whether it shows patterns associated with AI-generated or human-written text.

To start the service:

```bash
python app.py
```

The application runs at `http://127.0.0.1:5000`.

For setup instructions, see [RUNNING.md](RUNNING.md).

---

# Unit 7 — The Build

## What This Does

1. A writer submits text and a creator ID to `/submit`.
2. `detector.py::model_signal` measures the text's predictability using GPT-2.
3. `stylometry.py::style_signal` analyzes sentence-length variation, vocabulary variety, and punctuation.
4. `scoring.py::combine_signals` combines both scores.
5. `scoring.py::score_to_label` assigns human, unsure, or AI.
6. `audit.py` records the decision and its associated information.
7. The API returns a content ID, confidence score, both signal scores, and a reader-friendly explanation.

The system is intended to provide an estimate, not proof of authorship.

---

## Signals and Scoring

### Signal One — Model Signal

**What it measures:**

`detector.py::model_signal` uses GPT-2 perplexity to measure how predictable the submitted writing is.

The perplexity value is converted into a score between 0 and 1. Higher scores indicate that the writing appears more AI-like according to this signal.

**Why that might differ between human and AI writing:**

AI-generated writing can contain predictable language patterns because language models frequently select statistically likely words.

**What it cannot see:**

Predictability does not prove authorship. Human writing can also be predictable, especially when it is simple or formal. Edited AI writing can be less predictable.

### Signal Two — Style Signal

**What it measures:**

`stylometry.py::style_signal` measures three characteristics:

- Sentence-length variation
- Vocabulary variety using type-token ratio
- Punctuation density

**Why that might differ between human and AI writing:**

AI-generated writing may use regular sentence structures and consistent vocabulary patterns. Human writing can have greater variation.

**What it cannot see:**

Human writers can also use regular sentence structures, and AI-generated writing can be edited to imitate human variation.

These characteristics are not reliable proof of authorship.

### The Combining Rule

**The rule:**

I combine the model signal and style signal using an equally weighted average.

**The numbers:**

- Model weight: 0.50
- Style weight: 0.50

Formula:

`combined_score = (0.50 * model_score) + (0.50 * style_score)`

**Where it lives:**

`scoring.py::combine_signals`

**A case where my signals disagreed:**

One test produced:

- Model score: 0.6722
- Style score: 0.4904
- Combined score: 0.5813

The final score fell in the unsure range. This demonstrates how combining the signals can avoid a confident classification when the individual scores differ.

---

## Label Variants

| Label | Score range | Message |
|---|---|---|
| Human | 0.00–0.35 | This writing shows patterns that are more consistent with human-written text. |
| Unsure | Above 0.35 and below 0.65 | We are not confident whether this writing was produced by a person or AI. |
| AI | 0.65–1.00 | This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship. |

**Why I worded the unsure message this way:**

I wanted the system to admit uncertainty instead of making an unsupported accusation.

During earlier manual testing, all three labels were observed:

- Human: 0.3005
- Unsure: 0.5813
- AI: 0.7109

However, my later Unit 8 evaluation scenarios did not reproduce the human label.

---

## Sample Run

### A Submission

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"The system works well. It handles most cases correctly and provides good results. Users generally find it easy to use and understand.","creator_id":"siyani"}'
```

**Actual response:**

```json
{
  "confidence": 0.5813,
  "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
  "guess": "unsure",
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "model_score": 0.6722,
  "style_score": 0.4904
}
```

### An Appeal

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"e7db2c2c-3b27-479b-ad20-b31bd4129a81","reasoning":"I wrote this text myself and would like the result reviewed."}'
```

**Actual response:**

```json
{
  "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
  "message": "Your appeal has been recorded and is under review.",
  "status": "under_review"
}
```

The audit log recorded the original decision and a subsequent appeal event with the status `under_review`.

---

## How I Used AI

### Moment 1

**What I asked for:**

I asked AI to help debug my Flask `/submit` route when the style score kept returning `null`.

**What came back:**

AI helped identify problems with saving my updated `app.py` and connecting the stylometry and scoring functions.

**What I changed:**

I saved the corrected code and tested the endpoint to verify that both signals and the combined confidence score appeared in the response.

### Moment 2

**What I asked for:**

I asked AI to help implement and test the three classification labels and the appeal workflow.

**What came back:**

AI helped with `score_to_label`, `/appeal`, and example test requests.

**What I changed:**

I tested the API, verified the returned labels, and improved the handling of invalid submissions.

### Moment 3

**What I asked for:**

I used AI to help prepare the Unit 8 evaluation scenarios, interpret the results, and organize my README.

**What came back:**

AI generated synthetic human-style examples, AI-writing comparison examples, and explanations of the observed results.

**What I changed:**

I ran the evaluation commands myself and reported the observed outcomes. I identified the synthetic samples as AI-generated rather than presenting them as authentic human writing.

---

# Unit 8 — The Test

## Rate Limiting

I added rate limiting to protect the service from excessive submissions.

The configured limits are:

- 10 submissions per minute
- 200 submissions per day

I chose these limits because a normal user should not need to submit writing repeatedly within a short period.

### Rate-Limit Test

Command:

```bash
python run_attacks.py --flood 15
```

**Observed results:**

| Response | Requests |
|---|---:|
| HTTP 200 | 10 |
| HTTP 429 | 5 |
| Total | 15 |

After ten accepted submissions, the remaining five requests were blocked.

I also checked the audit log. The earlier log inspection showed 24 entries, including five rejected requests.

The rejection records included the creator ID, timestamp, rejection reason, and limit.

This demonstrates that rate limiting is functioning.

The current limiter uses in-memory storage. In a production environment, I would use shared persistent storage so limits remain consistent across restarts and multiple servers.

---

## Attack Run — Before

I ran the attack suite before improving request validation.

Source: `results/attack_run_2026-11-09_1809_before.md`

The before-run revealed important weaknesses in request handling.

### Before-Run Findings

**RQ06 — Invalid creator ID**

The request submitted a JSON object as the creator ID instead of a string.

The application accepted the request and returned HTTP 200 with a human classification.

**Verdict: BROKE**

**RQ07 — JSON Array Request**

The request sent a JSON array instead of a JSON object.

The application returned HTTP 500 because it attempted to call `.get()` on a list.

**Verdict: BROKE**

This was the most serious failure because malformed input caused an unhandled server error.

**RQ08–RQ12 — Invalid Requests**

These requests returned HTTP 400.

**Verdict: HELD**

**Flooding Test**

The first ten requests returned HTTP 200.

Requests eleven and twelve returned HTTP 429.

**Verdict: HELD**

The rate limiter successfully blocked excessive submissions.

### What Needed Improvement

The main problem was insufficient input validation in the submission route.

The application needed to verify that incoming JSON was an object and that the creator ID had the correct data type before processing the request.

The complete attack-by-attack before-run output is saved in `results/attack_run_2026-11-09_1809_before.md`. The remaining individual attacks still need manual HELD/BROKE assessment.

### Ten Audit Log Entries

The following nine entries were selected from the audit extract. They show false-positive classifications, evasion, prompt injection, unusual content, and rate-limit rejection.

```json
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
  }
]
```

These are nine distinct entries. One additional complete record must be added from `logs/audit.jsonl` to meet the requirement of ten entries.

### The Single Worst Outcome

The most concerning outcome was the false-positive behavior.

Six of the eight false-positive attack inputs in the after-run were classified as AI.

This is serious because a human writer could be incorrectly accused of using AI based on writing patterns that are not reliable proof of authorship.

I would be most concerned about explaining this result to a writer who submitted their own work.

---

## Run Log and Verdicts

I ran the following commands:

```bash
python run_eval.py --label before
python run_eval.py --label trial2
python run_eval.py --label trial3
```

The results were saved in:

- `results/run_2026-11-09_1851_before.md`
- `results/run_2026-11-09_1851_trial2.md`
- `results/run_2026-11-09_1851_trial3.md`

Each evaluation command ran three internal trials.

### Evaluation Results

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | At most 1 of 10 genuine human texts labeled AI | 10/10 synthetic human-style samples labeled AI | 10/10 | 10/10 | Synthetic test failed; genuine-human criterion not verified |
| 2. Score separation | AI mean at least 0.20 higher | 1/5 AI examples labeled AI | 1/5 | 1/5 | Numerical comparison pending |
| 3. Label coverage | All three labels | AI and unsure | AI and unsure | AI and unsure | Failed on selected inputs |
| 4. Appeals | 5/5 valid appeals under review and audited | 5/5 returned under_review in separate test | Not repeated | Not repeated | Response test passed; audit verification pending |
| 5. Bad inputs | 3/3 controlled responses without crashing | No crash observed | No crash observed | No crash observed | HTTP status verification pending |

### Real Output from One Trial

Source: `results/run_2026-11-09_1851_before.md`

Produced by `run_eval.py` calling the `/submit` endpoint in `app.py`.

```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.735,
  "model_score": 0.9011,
  "style_score": 0.5689,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship."
}
```

This was a synthetic human-style paragraph about going to the library.

### Appeals Test

I submitted five separate pieces of writing and appealed each returned content ID.

All five appeals returned HTTP 200 and `under_review`.

| Appeal | HTTP status | Appeal status |
|---|---|---|
| 1 | 200 | under_review |
| 2 | 200 | under_review |
| 3 | 200 | under_review |
| 4 | 200 | under_review |
| 5 | 200 | under_review |

The API response portion passed. The five corresponding audit entries still need to be verified.

---

## Diagnoses

### Criterion 1 — False Positives

All ten synthetic human-style samples received AI classifications.

One example produced:

- Model score: 0.9011
- Style score: 0.5689
- Combined score: 0.735

The model signal gave the writing a high AI score because it was predictable.

The combining rule assigned equal weight to both signals, resulting in a score above the AI threshold of 0.65.

The problem occurs in the model signal and combining rule.

The examples were AI-generated synthetic text, so these results do not establish the false-positive rate on genuine human writing.

### Criterion 2 — Score Separation

Four of the five AI examples received unsure classifications, while one received AI.

This indicates that the detector was not consistently confident about those AI-generated examples.

However, labels alone do not establish whether the mean AI score exceeded the mean comparison score by 0.20.

The numerical means must be calculated before declaring a pass or fail.

### Criterion 3 — Label Coverage

The evaluation produced AI and unsure labels but did not produce human.

The label mapping supports all three categories, but the selected inputs did not reach the human score range.

This is a problem with the tested score distribution and coverage.

### Criterion 4 — Appeals

The appeal endpoint accepted five valid requests and returned `under_review` for each one.

The route behaved correctly in this manual test.

The audit entries still need to be checked to confirm the full criterion.

### Criterion 5 — Bad Inputs

Missing and empty text were rejected without an observed crash.

The extremely long input was accepted and classified as AI.

The route handled these inputs without an observed server failure, but maximum input length validation could be improved.

### False-Positive Attacks

Six false-positive probes were classified as AI.

The model signal can treat predictable human-like writing as AI-generated.

The style signal can also assign higher scores to regular sentence patterns.

Because the combining rule uses equal weights, these signals can produce a confident AI classification.

### Evasion Attacks

Nine of ten evasion inputs returned unsure.

Changes in wording and writing patterns can affect perplexity and stylometric measurements.

This reduces the detector's confidence even when the underlying writing originated from AI.

### Prompt-Injection Attacks

The prompt-injection inputs produced human or unsure labels.

The results alone do not prove whether the injected instructions changed the detector's behavior.

The system should continue treating submitted writing as data rather than instructions.

### Malformed Requests

Most malformed requests were rejected with HTTP 400.

However, some unusual inputs were accepted and classified.

The route could use stronger validation for missing creator IDs, control characters, and unusual text.

### Flooding Attacks

The first ten flood submissions returned HTTP 200.

The next two returned HTTP 429.

This demonstrates that rate limiting blocked the excess requests.

---

## The Improvement

**What I changed:**

I strengthened request validation and added rate limiting to the submission endpoint.

The service returns controlled responses for malformed requests and limits repeated submissions.

The configured rate limits are ten submissions per minute and 200 per day.

**Which diagnosis pointed at it:**

The malformed-request and flooding attacks showed that the service needed stronger protection against invalid requests and excessive submissions.

These improvements address API reliability rather than authorship-detection accuracy.

### Before and After Comparison

I compared the results of two malformed-request attacks before and after improving input validation.

| Attack | Before | After | Result |
|---|---|---|---|
| RQ06 — creator_id is an object | HTTP 200 | HTTP 400 | Fixed |
| RQ07 — JSON array instead of object | HTTP 500 | HTTP 400 | Fixed |

**RQ06:**

Before the improvement, the application accepted a JSON object as the creator ID and returned HTTP 200.

After the improvement, the application rejected the invalid creator ID with HTTP 400.

The attack changed from BROKE to HELD.

**RQ07:**

Before the improvement, sending a JSON array caused an HTTP 500 error because the application attempted to call `.get()` on a list.

After the improvement, the application correctly rejected the JSON array with HTTP 400.

The attack changed from BROKE to HELD.

**Conclusion:**

Both malformed-request vulnerabilities were fixed.

The before-and-after results demonstrate that the input validation improvement made the submission endpoint more reliable.

---

## Attack Run — After

I ran the attack suite after the changes.

Source: `results/attack_run_2026-11-09_1838_after.md`

The after-run contained 56 requests.

No HTTP 500 server errors were observed.

### Attack Results

| Attack category | Observed result |
|---|---|
| Evasion EV01–EV10 | 9 unsure, 1 AI |
| False positives FP01–FP08 | 6 AI, 1 unsure, 1 human |
| Prompt injection PI01–PI06 | Mostly unsure; one human |
| Malformed content MF01–MF08 | 2 HTTP 400; 6 accepted and classified |
| Malformed requests RQ01–RQ12 | Mostly HTTP 400; missing creator ID accepted |
| Flood FL01_01–FL01_12 | 10 HTTP 200; 2 HTTP 429 |

### Confirmed Fixes

| Attack | Before verdict | After verdict |
|---|---|---|
| RQ06 | BROKE | HELD |
| RQ07 | BROKE | HELD |

The attack runner reported zero automatically marked BROKE outcomes in the after-run, but all 56 attacks still require manual HELD/BROKE assessment.

The full after-run report is saved in `results/attack_run_2026-11-09_1838_after.md`.

### Did It Help, and How Do I Know?

Yes, the input validation improvement helped.

RQ06 changed from HTTP 200 to HTTP 400.

RQ07 changed from HTTP 500 to HTTP 400.

These changes show that the application now rejects invalid creator IDs and JSON arrays instead of accepting them or crashing.

The flood test also demonstrated that rate limiting blocks excessive submissions.

However, classification problems remained.

Six false-positive probes were still labeled AI, and most evasion probes were classified as unsure.

The improvement made the API more reliable, but it did not solve the detector's accuracy problems.

---

## What's Still Broken

The detector still has several important limitations.

**False positives:** Human-style writing can receive high AI scores because predictable language is not unique to AI-generated text.

**Evasion:** Modified AI-generated writing can receive unsure classifications.

**Label coverage:** The selected Unit 8 evaluation inputs did not produce a human classification.

**Score separation:** The numerical mean-score difference still needs to be calculated.

**Appeal auditing:** The five manual appeal responses succeeded, but their corresponding audit records still need verification.

**Input validation:** Extremely long inputs and some unusual content can still be accepted and classified.

### What I Would Improve Next

I would collect more genuine human-written examples and verified AI-generated writing.

I would use this dataset to calibrate the detector and evaluate false-positive rates.

I would also improve the handling of unusually long submissions and malformed inputs.

I stopped short of changing the model thresholds because the available evaluation results do not provide enough evidence to justify a specific calibration change.

### The Trade I Would Make If This Ran for Real

I would rather classify uncertain writing as unsure than incorrectly accuse a human writer of using AI.

This would allow some AI-generated writing to avoid confident detection, but it would reduce the risk of unfairly accusing innocent writers.

---

## Submission Checklist

### Unit 7

- [x] Five acceptance criteria defined in `criteria.md`
- [x] Submission endpoint implemented
- [x] Two different scoring signals implemented
- [x] Three label variants implemented
- [x] Appeal endpoint implemented
- [x] Combining rule documented
- [x] Submission and appeal sample included
- [ ] Verify required commit count
- [ ] Submit repository URL

### Unit 8

- [x] Rate limiting implemented
- [x] HTTP 429 responses observed
- [x] Audit logging implemented
- [x] Attack suite executed
- [ ] Paste full before and after attack tables with manual verdicts
- [ ] Include ten complete audit-log entries
- [x] Three evaluation commands completed
- [x] Evaluation weaknesses documented
- [x] Improvement described
- [x] Before-and-after fixes confirmed
- [x] After-run results summarized
- [x] Remaining limitations and production tradeoff documented
- [ ] Verify five appeal audit entries
- [ ] Calculate mean-score separation
- [ ] Verify required commit count
- [ ] Submit the same repository URL as Unit 7

---

**How to run this project:** [RUNNING.md](RUNNING.md)
