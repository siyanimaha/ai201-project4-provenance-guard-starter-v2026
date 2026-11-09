# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:19
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `56933706-a761-4f9a-88ca-035f867c5586` | unsure | 0.382 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `733ff343-a564-4b52-bb16-4c616b1daacc` | unsure | 0.478 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `6f0d4fff-282f-4c7d-9f76-3b03af6b54a5` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `79f0cba1-128f-4093-a8b1-2ff455f63943` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `698cdceb-e982-4b20-8189-0830056bd56f` | unsure | 0.369 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `10c0f9d6-fbf1-4b08-8682-e24598e4ca3d` | unsure | 0.474 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `f596162d-6e38-4f2b-81e5-459b883de68b` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f1ab9c7f-6bdb-44dd-82cb-32c6c01615ad` | unsure | 0.357 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1c47048d-a6c9-4e51-a4ca-74fd9dec7d06` | unsure | 0.602 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d8abe826-6f0a-40ee-a974-c868d05eb913` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `fae1a8c3-00b7-469b-a963-7e3f5478220e` | unsure | 0.583 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a17a89f8-d9dd-4410-80ed-c63dce289d04` | ai | 0.683 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `bbc13887-8b74-4781-9af2-42b169836863` | ai | 0.700 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c29a3938-ec88-409b-9dcc-73f192d435ea` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `9bff307c-bae9-4cd8-ba77-71502d6ed2a9` | ai | 0.718 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `44c1918e-d3d3-407a-b8fe-2ab83f6ce07b` | ai | 0.699 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b32ad7b4-74fc-44a7-9570-19cfa97efb6e` | ai | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `1478b43f-bb2d-4f8f-87d2-9ee6f1e7f663` | human | 0.283 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e2c23ce1-fc0e-4864-bb2a-8fba1d4b3d45` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `5ca30375-3b45-4167-8074-1d06867fa448` | human | 0.293 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b9444f12-616b-4062-8641-d8a1dfd0c1be` | unsure | 0.566 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a20ea51c-c36c-43dc-b9c7-1792326ef982` | unsure | 0.510 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `24cdea11-191a-422b-8726-cc186339374d` | unsure | 0.510 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ef2eadd6-8d08-4900-866f-6a940bc7eb9a` | unsure | 0.556 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `714f3cf7-4a58-4beb-91c8-f7441c274ee8` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `8a952791-f203-4f26-87df-88ed80b86efb` | human | 0.339 |  |
| MF05 | malformed | text is a very long single word | 200 | `37f55794-f1be-4461-b220-eea9d11e0d77` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `1ac36fb9-bedb-4346-9ab1-0fd760b8b90c` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `68fa09cf-7075-4f88-9aa2-1551aa55dc8c` | ai | 0.937 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `5e9699ee-1915-4e6e-be88-5421e22be118` | ai | 0.890 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `d61bfec7-2de9-4076-a08b-1c1dc56657c5` | unsure | 0.423 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `b5acd5f6-c1b3-44c7-a9a8-b59450d29282` | human | 0.265 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a76107c2-9769-467b-9c6d-c6f166d0d74c` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ba67634f-81fb-4b43-8c87-18f3ebe66911` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8ae1b814-2c6c-4b06-989a-72c5f4fde932` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3be0f1bc-582e-4bfc-a6fd-5f5cb01aa1a8` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b85cfcdc-c690-4767-b75b-3bdf4de16a2a` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fa2afac2-ac7e-4484-8619-b44ff26d3fca` | human | 0.317 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b38bc0b7-e817-4a56-9c35-ad296b07b5d5` | human | 0.317 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ae08eebe-e8ec-450b-b106-3b263228eced` | human | 0.317 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6a45036f-f583-4193-a53c-94ed6a499aac` | human | 0.317 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81ac6477-1e68-4822-9f11-9b62d3fe82ed` | human | 0.317 |  |
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
  "content_id": "56933706-a761-4f9a-88ca-035f867c5586",
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
  "content_id": "733ff343-a564-4b52-bb16-4c616b1daacc",
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
  "content_id": "6f0d4fff-282f-4c7d-9f76-3b03af6b54a5",
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
  "content_id": "79f0cba1-128f-4093-a8b1-2ff455f63943",
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
  "content_id": "698cdceb-e982-4b20-8189-0830056bd56f",
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
  "content_id": "10c0f9d6-fbf1-4b08-8682-e24598e4ca3d",
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
  "content_id": "f596162d-6e38-4f2b-81e5-459b883de68b",
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
  "content_id": "f1ab9c7f-6bdb-44dd-82cb-32c6c01615ad",
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
  "content_id": "1c47048d-a6c9-4e51-a4ca-74fd9dec7d06",
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
  "content_id": "d8abe826-6f0a-40ee-a974-c868d05eb913",
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
  "content_id": "fae1a8c3-00b7-469b-a963-7e3f5478220e",
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
  "content_id": "a17a89f8-d9dd-4410-80ed-c63dce289d04",
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
  "content_id": "bbc13887-8b74-4781-9af2-42b169836863",
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
  "content_id": "c29a3938-ec88-409b-9dcc-73f192d435ea",
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
  "content_id": "9bff307c-bae9-4cd8-ba77-71502d6ed2a9",
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
  "content_id": "44c1918e-d3d3-407a-b8fe-2ab83f6ce07b",
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
  "content_id": "b32ad7b4-74fc-44a7-9570-19cfa97efb6e",
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
  "content_id": "1478b43f-bb2d-4f8f-87d2-9ee6f1e7f663",
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
  "content_id": "e2c23ce1-fc0e-4864-bb2a-8fba1d4b3d45",
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
  "content_id": "5ca30375-3b45-4167-8074-1d06867fa448",
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
  "content_id": "b9444f12-616b-4062-8641-d8a1dfd0c1be",
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
  "content_id": "a20ea51c-c36c-43dc-b9c7-1792326ef982",
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
  "content_id": "24cdea11-191a-422b-8726-cc186339374d",
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
  "content_id": "ef2eadd6-8d08-4900-866f-6a940bc7eb9a",
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
  "content_id": "714f3cf7-4a58-4beb-91c8-f7441c274ee8",
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
  "content_id": "8a952791-f203-4f26-87df-88ed80b86efb",
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
  "content_id": "37f55794-f1be-4461-b220-eea9d11e0d77",
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
  "content_id": "1ac36fb9-bedb-4346-9ab1-0fd760b8b90c",
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
  "content_id": "68fa09cf-7075-4f88-9aa2-1551aa55dc8c",
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
  "content_id": "5e9699ee-1915-4e6e-be88-5421e22be118",
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
  "content_id": "d61bfec7-2de9-4076-a08b-1c1dc56657c5",
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
  "content_id": "b5acd5f6-c1b3-44c7-a9a8-b59450d29282",
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
  "content_id": "a76107c2-9769-467b-9c6d-c6f166d0d74c",
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
  "content_id": "ba67634f-81fb-4b43-8c87-18f3ebe66911",
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
  "content_id": "8ae1b814-2c6c-4b06-989a-72c5f4fde932",
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
  "content_id": "3be0f1bc-582e-4bfc-a6fd-5f5cb01aa1a8",
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
  "content_id": "b85cfcdc-c690-4767-b75b-3bdf4de16a2a",
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
  "content_id": "fa2afac2-ac7e-4484-8619-b44ff26d3fca",
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
  "content_id": "b38bc0b7-e817-4a56-9c35-ad296b07b5d5",
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
  "content_id": "ae08eebe-e8ec-450b-b106-3b263228eced",
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
  "content_id": "6a45036f-f583-4193-a53c-94ed6a499aac",
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
  "content_id": "81ac6477-1e68-4822-9f11-9b62d3fe82ed",
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
