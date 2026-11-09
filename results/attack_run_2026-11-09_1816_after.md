# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:16
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `5f1e3deb-e2c3-4ec4-b6fb-432b3abf1284` | unsure | 0.382 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `596f34d0-c8b5-489e-bacb-3f90398fcfcb` | unsure | 0.478 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8ab8fc62-0af7-445d-81b8-2604e6b6c05a` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `8ea699fb-4718-480f-b14f-bc40284593a1` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8c861eb5-128a-4373-9f38-2decad2648b0` | unsure | 0.369 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `7e374877-24d4-4312-9fbe-0f9383ff5655` | unsure | 0.474 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1790b6ad-71b8-4010-a848-b063f1ebe59a` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `04ed8125-ff8e-4745-9d90-b03769cad14b` | unsure | 0.357 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `6f1a4f5b-2fe1-4f87-a1cd-4c675bcae9de` | unsure | 0.602 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `19d9641e-5385-4153-b05e-16f6e92571e0` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `00e43c83-c742-4fe3-8fef-6de40f39ca08` | unsure | 0.583 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `444a12b8-312f-4289-af70-dd99414e27a0` | ai | 0.683 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `caa0dd9e-f81f-4522-8140-bfb4dcc9d7f2` | ai | 0.700 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b6d35266-48dc-43d6-9604-c33f437d1d83` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `3f340f67-88b8-4658-a5cf-fb6201268ad7` | ai | 0.718 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `fa074fb9-70b3-48f7-a53e-8660b74ce06c` | ai | 0.699 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `86d88361-9c8a-48bf-b95e-562f397909f5` | ai | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `3f26d94c-077a-48ec-90e4-1bb883ecbf1d` | human | 0.283 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `4a058e3f-49b2-447c-8f36-2cc7e66bb3b1` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3bdaf99b-f4c8-4f35-aae2-f415ebd7aa22` | human | 0.293 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `1a7e17fa-7960-4afb-8ac9-7b6f17a245aa` | unsure | 0.566 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `37a54c30-a7e9-4f33-98a1-252b0a7d7d98` | unsure | 0.510 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `792fb326-a060-45a3-9e4f-ef6c5f4244db` | unsure | 0.510 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `594e2331-8d75-49f9-9c08-8fe3cf1ae434` | unsure | 0.556 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `543da34d-513e-4a63-8079-7635685c4b3f` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `a5368b29-0908-40b6-8b36-213a8b396579` | human | 0.339 |  |
| MF05 | malformed | text is a very long single word | 200 | `efa9e24d-2f36-45f6-a9fc-7c093632d130` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `bd89bdfc-d00a-4eea-b98d-9f90105fe61a` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `9fa1a23e-79c7-405a-a8a2-f9ce08e5d2d5` | ai | 0.937 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `cbab2149-c2e2-4c51-a875-484c2ca9c4e0` | ai | 0.890 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `f6ddd61c-e8d4-4468-8c0b-a94b69f2008d` | unsure | 0.423 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `09191c1d-ce40-4854-8943-50809658435f` | human | 0.265 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4100e88d-dcc3-4eee-99ed-f6e380dad4a3` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7f068e57-5832-4884-a7d2-ffdecc6f7310` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bf726bf3-3801-4d5a-9be1-6f983e3f9c77` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eb859ccb-3d09-4f6a-a57b-8efe4419c678` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7862754f-d1e7-48cd-b4c5-8af10b271ca6` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9f484b06-cf78-4e29-9dde-6ef791edf7e1` | human | 0.317 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ee7474d-0e71-48c1-b076-4ab5521fc8d2` | human | 0.317 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f267e4d8-e923-4536-a372-f96842828311` | human | 0.317 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5a72ae2d-6a36-4edf-b617-ce2e17877769` | human | 0.317 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c1ccd81a-1c8b-44a7-a663-2195a6841036` | human | 0.317 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "5f1e3deb-e2c3-4ec4-b6fb-432b3abf1284",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3821,
  "model_score": 0.1635,
  "style_score": 0.6006,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "596f34d0-c8b5-489e-bacb-3f90398fcfcb",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4783,
  "model_score": 0.5943,
  "style_score": 0.3622,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "8ab8fc62-0af7-445d-81b8-2604e6b6c05a",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.585,
  "model_score": 0.6662,
  "style_score": 0.5037,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "8ea699fb-4718-480f-b14f-bc40284593a1",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.601,
  "model_score": 0.6114,
  "style_score": 0.5906,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "8c861eb5-128a-4373-9f38-2decad2648b0",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3693,
  "model_score": 0.3212,
  "style_score": 0.4175,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "7e374877-24d4-4312-9fbe-0f9383ff5655",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4738,
  "model_score": 0.5727,
  "style_score": 0.375,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1790b6ad-71b8-4010-a848-b063f1ebe59a",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6131,
  "model_score": 0.5862,
  "style_score": 0.6399,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "04ed8125-ff8e-4745-9d90-b03769cad14b",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3574,
  "model_score": 0.2452,
  "style_score": 0.4697,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "6f1a4f5b-2fe1-4f87-a1cd-4c675bcae9de",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.602,
  "model_score": 0.7042,
  "style_score": 0.4999,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "19d9641e-5385-4153-b05e-16f6e92571e0",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8614,
  "model_score": 0.9792,
  "style_score": 0.7435,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "00e43c83-c742-4fe3-8fef-6de40f39ca08",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5826,
  "model_score": 0.6175,
  "style_score": 0.5476,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "444a12b8-312f-4289-af70-dd99414e27a0",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6829,
  "model_score": 0.7387,
  "style_score": 0.6271,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "caa0dd9e-f81f-4522-8140-bfb4dcc9d7f2",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6996,
  "model_score": 0.8051,
  "style_score": 0.594,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "b6d35266-48dc-43d6-9604-c33f437d1d83",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6867,
  "model_score": 0.8329,
  "style_score": 0.5405,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "3f340f67-88b8-4658-a5cf-fb6201268ad7",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7183,
  "model_score": 0.8005,
  "style_score": 0.6361,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "fa074fb9-70b3-48f7-a53e-8660b74ce06c",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6987,
  "model_score": 0.8814,
  "style_score": 0.5161,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "86d88361-9c8a-48bf-b95e-562f397909f5",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6979,
  "model_score": 0.8816,
  "style_score": 0.5142,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "3f26d94c-077a-48ec-90e4-1bb883ecbf1d",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2835,
  "model_score": 0.3223,
  "style_score": 0.2447,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "4a058e3f-49b2-447c-8f36-2cc7e66bb3b1",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4393,
  "model_score": 0.4625,
  "style_score": 0.416,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "3bdaf99b-f4c8-4f35-aae2-f415ebd7aa22",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2929,
  "model_score": 0.2044,
  "style_score": 0.3815,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "1a7e17fa-7960-4afb-8ac9-7b6f17a245aa",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5663,
  "model_score": 0.5943,
  "style_score": 0.5383,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "37a54c30-a7e9-4f33-98a1-252b0a7d7d98",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5096,
  "model_score": 0.4998,
  "style_score": 0.5195,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "792fb326-a060-45a3-9e4f-ef6c5f4244db",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5099,
  "model_score": 0.6401,
  "style_score": 0.3796,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "594e2331-8d75-49f9-9c08-8fe3cf1ae434",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5561,
  "model_score": 0.5583,
  "style_score": 0.5539,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "543da34d-513e-4a63-8079-7635685c4b3f",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.3333,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "a5368b29-0908-40b6-8b36-213a8b396579",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3389,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "efa9e24d-2f36-45f6-a9fc-7c093632d130",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8321,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "bd89bdfc-d00a-4eea-b98d-9f90105fe61a",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "9fa1a23e-79c7-405a-a8a2-f9ce08e5d2d5",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9374,
  "model_score": 0.9064,
  "style_score": 0.9683,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "cbab2149-c2e2-4c51-a875-484c2ca9c4e0",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8896,
  "model_score": 0.9876,
  "style_score": 0.7915,
  "label": "This writing shows patterns that are more consistent with AI-generated text, but this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "f6ddd61c-e8d4-4468-8c0b-a94b69f2008d",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4227,
  "model_score": 0.2395,
  "style_score": 0.606,
  "label": "We are not confident whether this writing was produced by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "09191c1d-ce40-4854-8943-50809658435f",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2652,
  "model_score": 0.0492,
  "style_score": 0.4813,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4100e88d-dcc3-4eee-99ed-f6e380dad4a3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "7f068e57-5832-4884-a7d2-ffdecc6f7310",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "bf726bf3-3801-4d5a-9be1-6f983e3f9c77",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "eb859ccb-3d09-4f6a-a57b-8efe4419c678",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "7862754f-d1e7-48cd-b4c5-8af10b271ca6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "9f484b06-cf78-4e29-9dde-6ef791edf7e1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "1ee7474d-0e71-48c1-b076-4ab5521fc8d2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "f267e4d8-e923-4536-a372-f96842828311",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "5a72ae2d-6a36-4edf-b617-ce2e17877769",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "c1ccd81a-1c8b-44a7-a663-2195a6841036",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3173,
  "model_score": 0.0287,
  "style_score": 0.606,
  "label": "This writing shows patterns that are more consistent with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
