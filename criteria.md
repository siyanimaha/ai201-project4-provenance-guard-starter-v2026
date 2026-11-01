# Acceptance criteria — Provenance Guard

## 1. Human writing should rarely be labeled as AI

Of 10 pieces of human-written text, no more than 1 should be labeled as AI.

**Why this target:** I chose 1 out of 10 because falsely labeling a real person's writing as AI is worse than missing some AI-written text. I want the system to be careful before accusing someone.

---

## 2. Human and AI writing should have different scores

The average score for clearly AI-written text should be at least 0.20 higher than the average score for clearly human-written text.

**Why this target:** I chose a difference of 0.20 because I want the two types of writing to have a noticeable difference in their scores instead of getting almost the same results.

---

## 3. All three labels should be reachable

When testing different types of writing, the system should be able to produce all 3 labels: human, unsure, and AI.

**Why this target:** I chose all 3 because each label has a purpose. If one of the labels can never appear, then the system is not using the full decision range.

---

## 4. Appeals should always be recorded

For 5 test appeals with valid content IDs, all 5 should change the submission status to under_review and be recorded in the audit log.

**Why this target:** I chose 5 out of 5 because an appeal is important when the system may have made a wrong decision. A valid appeal should never disappear or fail to be recorded.

---

## 5. Bad input should not crash the service

For 3 bad-input tests—missing text, empty text, and extremely long text—the service should return a controlled response every time instead of crashing.

**Why this target:** I chose all 3 because users can send incorrect input, and the service should handle those situations safely instead of stopping or giving a server error.
**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->



**Why this target:**



---

## 2.

<!-- Your criterion. -->



**Why this target:**



---

## 3.

<!-- Your criterion. -->



**Why this target:**



---

## 4.

<!-- Your criterion. -->



**Why this target:**



---

## 5.

<!-- Your criterion. -->



**Why this target:**



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
