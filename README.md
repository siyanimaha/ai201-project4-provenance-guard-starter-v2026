# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

1. A writer sends their text and creator ID to the `/submit` endpoint.
2. `detector.py::model_signal` checks how predictable the text is and produces a model score from 0 to 1.
3. `stylometry.py::style_signal` examines writing patterns such as sentence-length variation, vocabulary variety, and punctuation.
4. `scoring.py::combine_signals` combines the model score and style score into one confidence score.
5. `scoring.py::score_to_label` converts the combined score into a human, unsure, or AI result.
6. `audit.py` records the submission, signal scores, final decision, and content ID in the audit log.
7. The `/submit` endpoint returns the content ID, scores, guess, confidence, and reader-friendly label to the writer.


---

## Signals and Scoring

### Signal one — the model signal

**What it measures:**  
`detector.py::model_signal` measures how predictable the text is to GPT-2. It converts the text's perplexity into a score from 0 to 1, where a higher score means the text looks more AI-like.

**Why that might differ between human and AI writing:**  
AI-generated writing can be more predictable because language models often choose common and statistically likely word patterns.

**What it can't see:**  
Predictability does not prove authorship. Simple or conventional human writing can also be predictable and may receive a high AI score. Unusual or heavily edited AI writing may receive a lower score.

### Signal two — the style signal

**What it measures:**  
`stylometry.py::style_signal` measures sentence-length variation, vocabulary variety using type-token ratio, and punctuation density.

**Why that might differ between human and AI writing:**  
AI writing can have more regular sentence structures and writing patterns, while human writing may contain more variation.

**What it can't see:**  
Writing style is not unique to humans or AI. A human can write in a very regular style, and AI-generated text can be edited to include more variation.

### The combining rule

**The rule:**  
I combine the model signal and style signal using a weighted average. Both signals receive equal weight. When the signals disagree, the combined score moves toward the middle, which represents uncertainty rather than automatically accusing the writer of using AI.

**The numbers:**  
Model signal weight = 0.50  
Style signal weight = 0.50  

Combined score = (0.50 × model score) + (0.50 × style score)

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**  
One test produced a model score of 0.6722 and a style score of 0.4904. The signals did not completely agree. The combining rule produced 0.5813, which fell into the unsure range. This is useful because disagreement between the signals should result in uncertainty instead of a strong accusation.

---
### Signal one — the model signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

### Signal two — the style signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---
## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | This writing shows patterns that are more consistent with human-written text. |
| unsure | 0.35 – 0.65 | We are not confident whether this writing was produced by a person or AI. |
| high-confidence AI | 0.65 – 1.00 | This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship. |

**Why I worded the "unsure" one this way:**  
I wanted the message to clearly admit that the system does not know the answer. It avoids accusing the writer of using AI when the evidence is not strong enough.

During testing, all three labels were reachable:
- Human: 0.3005
- Unsure: 0.5813
- AI: 0.7109


---

## Sample Run

## Sample Run

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"The system works well. It handles most cases correctly and provides good results. Users generally find it easy to use and understand.","creator_id":"siyani"}'
```

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

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"e7db2c2c-3b27-479b-ad20-b31bd4129a81","reasoning":"I wrote this text myself and would like the result reviewed."}'
```

```json
{
  "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
  "message": "Your appeal has been recorded and is under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```json
{
  "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
  "creator_id": "siyani",
  "guess": "unsure",
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "model_score": 0.6722,
  "style_score": 0.4904,
  "combined_score": 0.5813,
  "status": "decided"
}
{
  "content_id": "e7db2c2c-3b27-479b-ad20-b31bd4129a81",
  "creator_id": "siyani",
  "event": "appeal",
  "reasoning": "I wrote this text myself and would like the result reviewed.",
  "status": "under_review"
}
```


---

## How I Used AI

**Moment 1**

- **What I asked for:** I asked AI to help me debug my Flask `/submit` route when the style score kept returning `null`.
- **What came back:** AI helped me identify that my updated `app.py` had not been saved and helped me connect `stylometry.py::style_signal` and `scoring.py::combine_signals` to the submission route.
- **What I changed:** I saved and tested the code myself and verified that the API returned both signal scores and the combined confidence score.

**Moment 2**

- **What I asked for:** I asked AI for help implementing and testing the three labels and the appeal workflow.
- **What came back:** AI helped me connect `score_to_label` to the API, implement `/appeal`, and create test requests.
- **What I changed:** I tested human, unsure, and AI results myself, verified the appeal appeared in the audit log, and added input handling after an empty submission caused an error.
<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
