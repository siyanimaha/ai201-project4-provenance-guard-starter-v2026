# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:25
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `deae0793-2efc-4c38-93d2-10d6110ea756` | unsure | 0.382 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9149cf7d-20ec-4613-a8c3-9d3ae5509526` | unsure | 0.478 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4abf87a5-ace6-474d-b304-9171407514c3` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `bbe64b16-e86f-489b-96c2-419447653817` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `ed5899d1-2e11-4078-921e-1742b79dce67` | unsure | 0.369 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `1b01eb12-32e8-4559-aec1-d56f5e8d61f7` | unsure | 0.474 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `97e90434-81e5-4a51-8729-917cd58a61be` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c7e46d34-540b-4ff5-85bb-c95f43632b0a` | unsure | 0.357 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4d6f9083-f0cb-476e-a1af-a56d25ee8bcc` | unsure | 0.602 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e53dbce9-4672-4ea5-bb8e-d6939a14ad6f` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `e802271d-40c0-477f-90e0-d25eb15bf97d` | unsure | 0.583 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `2770672c-f5f7-4b36-aa26-bafd3e80d913` | ai | 0.683 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `bb318e37-36c1-4ea6-a431-9c3eb5013224` | ai | 0.700 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4ebca1a8-aa26-4341-83a0-a8d69baa872b` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `fd3e8f87-bcf6-4c2b-83c2-ae97462d2869` | ai | 0.718 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `3f606ba8-d359-4b1d-b0c4-e0a579a8c816` | ai | 0.699 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `7bda910a-b6b9-4b2a-b61f-7985b98dfc22` | ai | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `04b50f8d-3124-4315-b525-08af5509c755` | human | 0.283 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1f10d9f9-f0f0-4a32-8f18-55b5a001918f` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `7ed00475-014e-4046-adb9-8aaf25bf2905` | human | 0.293 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `965b02a4-be27-416d-96d9-e0954e078565` | unsure | 0.566 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `281bd0ab-e78d-4bce-8d35-ebfbfb435518` | unsure | 0.510 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `3ced6671-4d29-409d-9a7e-93550ae0962e` | unsure | 0.510 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `f104d4c4-c380-4a05-96f4-b037ffb66463` | unsure | 0.556 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `67bf1a52-6bd6-462d-aa41-59334c5f5421` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `de92dde7-e2a9-4d2d-ba94-35f7df0e6a42` | human | 0.339 |  |
| MF05 | malformed | text is a very long single word | 200 | `008acf23-6833-428c-8950-89d84065070e` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `532518e5-338a-479c-900a-05aaf8fd6274` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `f150b13a-296e-4ec8-a5f9-8421b53c402d` | ai | 0.937 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `c2b075c7-5fb0-46cd-a86b-937ef213bfdc` | ai | 0.890 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `63cbe378-a511-4b8a-b90b-84dddaecc7cb` | unsure | 0.423 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `4aac1323-11a0-4da2-8ae9-2c2f9e1b5b61` | human | 0.265 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7180ac07-d286-432b-9143-2177cfb39b1d` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0c2fca27-2cca-4dbc-96a3-e031ea1041a5` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4b272a8a-5048-47f7-a4c0-61b8a086a289` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbfbc488-db7c-4c1e-ae24-8f1a1fbae3ca` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `01c3d395-eed6-4a82-b22f-bf24d454dbad` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `08a2e3c1-a4fb-40e5-9f76-03b5f3558996` | human | 0.317 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9d4c63e3-65bd-4cf9-87ec-438bd3b3a9a2` | human | 0.317 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e048cd95-feb8-4fc2-a2a8-177a7d792c6e` | human | 0.317 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `23b904d5-cd72-4518-bf39-d221b7ca75df` | human | 0.317 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `69134d21-8d94-4549-8332-dc6308a90e2e` | human | 0.317 |  |
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
  "content_id": "deae0793-2efc-4c38-93d2-10d6110ea756",
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
  "content_id": "9149cf7d-20ec-4613-a8c3-9d3ae5509526",
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
  "content_id": "4abf87a5-ace6-474d-b304-9171407514c3",
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
  "content_id": "bbe64b16-e86f-489b-96c2-419447653817",
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
  "content_id": "ed5899d1-2e11-4078-921e-1742b79dce67",
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
  "content_id": "1b01eb12-32e8-4559-aec1-d56f5e8d61f7",
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
  "content_id": "97e90434-81e5-4a51-8729-917cd58a61be",
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
  "content_id": "c7e46d34-540b-4ff5-85bb-c95f43632b0a",
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
  "content_id": "4d6f9083-f0cb-476e-a1af-a56d25ee8bcc",
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
  "content_id": "e53dbce9-4672-4ea5-bb8e-d6939a14ad6f",
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
  "content_id": "e802271d-40c0-477f-90e0-d25eb15bf97d",
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
  "content_id": "2770672c-f5f7-4b36-aa26-bafd3e80d913",
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
  "content_id": "bb318e37-36c1-4ea6-a431-9c3eb5013224",
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
  "content_id": "4ebca1a8-aa26-4341-83a0-a8d69baa872b",
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
  "content_id": "fd3e8f87-bcf6-4c2b-83c2-ae97462d2869",
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
  "content_id": "3f606ba8-d359-4b1d-b0c4-e0a579a8c816",
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
  "content_id": "7bda910a-b6b9-4b2a-b61f-7985b98dfc22",
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
  "content_id": "04b50f8d-3124-4315-b525-08af5509c755",
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
  "content_id": "1f10d9f9-f0f0-4a32-8f18-55b5a001918f",
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
  "content_id": "7ed00475-014e-4046-adb9-8aaf25bf2905",
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
  "content_id": "965b02a4-be27-416d-96d9-e0954e078565",
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
  "content_id": "281bd0ab-e78d-4bce-8d35-ebfbfb435518",
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
  "content_id": "3ced6671-4d29-409d-9a7e-93550ae0962e",
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
  "content_id": "f104d4c4-c380-4a05-96f4-b037ffb66463",
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
  "content_id": "67bf1a52-6bd6-462d-aa41-59334c5f5421",
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
  "content_id": "de92dde7-e2a9-4d2d-ba94-35f7df0e6a42",
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
  "content_id": "008acf23-6833-428c-8950-89d84065070e",
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
  "content_id": "532518e5-338a-479c-900a-05aaf8fd6274",
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
  "content_id": "f150b13a-296e-4ec8-a5f9-8421b53c402d",
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
  "content_id": "c2b075c7-5fb0-46cd-a86b-937ef213bfdc",
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
  "content_id": "63cbe378-a511-4b8a-b90b-84dddaecc7cb",
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
  "content_id": "4aac1323-11a0-4da2-8ae9-2c2f9e1b5b61",
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
  "content_id": "7180ac07-d286-432b-9143-2177cfb39b1d",
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
  "content_id": "0c2fca27-2cca-4dbc-96a3-e031ea1041a5",
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
  "content_id": "4b272a8a-5048-47f7-a4c0-61b8a086a289",
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
  "content_id": "dbfbc488-db7c-4c1e-ae24-8f1a1fbae3ca",
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
  "content_id": "01c3d395-eed6-4a82-b22f-bf24d454dbad",
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
  "content_id": "08a2e3c1-a4fb-40e5-9f76-03b5f3558996",
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
  "content_id": "9d4c63e3-65bd-4cf9-87ec-438bd3b3a9a2",
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
  "content_id": "e048cd95-feb8-4fc2-a2a8-177a7d792c6e",
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
  "content_id": "23b904d5-cd72-4518-bf39-d221b7ca75df",
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
  "content_id": "69134d21-8d94-4549-8332-dc6308a90e2e",
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
