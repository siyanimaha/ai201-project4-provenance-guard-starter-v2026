# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:21
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `56375ba6-4390-49c8-aa92-15ad3222fe5d` | unsure | 0.382 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `0e634cde-e1bb-4fbc-84ae-9e1b7496c753` | unsure | 0.478 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `e98afea9-04c4-4d56-9d91-aec75c13cd86` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `51f4d971-247a-49ed-8250-d63c13ad2b06` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `aac605e1-1a0c-4ef6-ba15-9b3efbfa7e5a` | unsure | 0.369 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `20a81388-77d4-44ec-a220-b2d714652b9a` | unsure | 0.474 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `915a2748-9713-47fd-b492-db4cbb41db02` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `2afd9afb-65e8-48bd-bdfd-470f18abad9c` | unsure | 0.357 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `fbc8b242-8fe5-499b-91b5-c2e3c2714bc3` | unsure | 0.602 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d63d636d-24c9-40ad-bdd4-53ddf607e367` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3875e8ce-78a8-47ae-8e42-bc2036c22440` | unsure | 0.583 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `d37193f0-2772-4fd3-80e9-e3de4dc3d0c2` | ai | 0.683 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `26a75341-ac49-4bfa-a344-fe01e8c9b04e` | ai | 0.700 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `f57832fd-6fbc-44bd-a2f6-301ba91684d5` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `d0390c44-9bb1-4d93-aee2-ac5ea1803bae` | ai | 0.718 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `b13fa2d8-5e2e-4bdf-8bd6-84a1c648d52c` | ai | 0.699 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `90bd69fd-f466-4447-b699-efe673596338` | ai | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `0e22a963-4a14-45e6-ad58-31f63da2a083` | human | 0.283 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `0eaf7808-e627-4c38-87b7-47e8ee4eb299` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `770a2ff5-b359-4fc4-9aa1-814c5fe36b63` | human | 0.293 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2fa481fc-d1e9-484f-9786-c98d8911ee12` | unsure | 0.566 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `16f6cb34-ac7d-4254-a1fe-a17a535cdffc` | unsure | 0.510 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `15df94cd-bd95-44e8-8f0e-4f3605f228b5` | unsure | 0.510 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `b30fedc1-1342-49fb-ae1e-07c875888fa9` | unsure | 0.556 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `a3b8ff2d-6949-47f1-a905-920df5865382` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `b8e9edf2-39be-4b16-9591-cf20b0f0acfb` | human | 0.339 |  |
| MF05 | malformed | text is a very long single word | 200 | `8c363292-06d8-4efd-926e-480a262840a8` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `bd8fed42-b03a-4048-b9de-2afcd8cd3639` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `ea12dbd6-4685-4fb7-afde-8d232e3c6d03` | ai | 0.937 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `e75f4683-18ea-4749-8345-07d4517a5318` | ai | 0.890 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `28dedbf4-8c30-4a13-acdd-bf77e3d204c8` | unsure | 0.423 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `896d9ed6-4c2c-425c-b619-f7dcec40123d` | human | 0.265 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `17fd1ca4-3f0f-40a4-b507-f47bb3cfe323` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5489757e-4cf5-4aca-8a93-0872cdc32f33` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `16b885b9-b598-45c0-8f9d-39136d9f5153` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `202487f3-6ab4-44d4-88d0-dbdb5cd4ef7b` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6047754d-96b1-41aa-921f-001aff6ee09e` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fafb3631-694d-41d6-833a-fa5cd4234493` | human | 0.317 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fd5888b2-54c5-46e0-98f8-bd3eccc7d514` | human | 0.317 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ba0582c3-b14b-484f-8bd2-2574baa2324d` | human | 0.317 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4ab17026-ea34-4f5c-804c-29abf5071260` | human | 0.317 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `04d39eb0-a7d0-4209-8351-20c9b895e437` | human | 0.317 |  |
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
  "content_id": "56375ba6-4390-49c8-aa92-15ad3222fe5d",
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
  "content_id": "0e634cde-e1bb-4fbc-84ae-9e1b7496c753",
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
  "content_id": "e98afea9-04c4-4d56-9d91-aec75c13cd86",
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
  "content_id": "51f4d971-247a-49ed-8250-d63c13ad2b06",
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
  "content_id": "aac605e1-1a0c-4ef6-ba15-9b3efbfa7e5a",
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
  "content_id": "20a81388-77d4-44ec-a220-b2d714652b9a",
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
  "content_id": "915a2748-9713-47fd-b492-db4cbb41db02",
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
  "content_id": "2afd9afb-65e8-48bd-bdfd-470f18abad9c",
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
  "content_id": "fbc8b242-8fe5-499b-91b5-c2e3c2714bc3",
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
  "content_id": "d63d636d-24c9-40ad-bdd4-53ddf607e367",
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
  "content_id": "3875e8ce-78a8-47ae-8e42-bc2036c22440",
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
  "content_id": "d37193f0-2772-4fd3-80e9-e3de4dc3d0c2",
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
  "content_id": "26a75341-ac49-4bfa-a344-fe01e8c9b04e",
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
  "content_id": "f57832fd-6fbc-44bd-a2f6-301ba91684d5",
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
  "content_id": "d0390c44-9bb1-4d93-aee2-ac5ea1803bae",
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
  "content_id": "b13fa2d8-5e2e-4bdf-8bd6-84a1c648d52c",
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
  "content_id": "90bd69fd-f466-4447-b699-efe673596338",
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
  "content_id": "0e22a963-4a14-45e6-ad58-31f63da2a083",
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
  "content_id": "0eaf7808-e627-4c38-87b7-47e8ee4eb299",
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
  "content_id": "770a2ff5-b359-4fc4-9aa1-814c5fe36b63",
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
  "content_id": "2fa481fc-d1e9-484f-9786-c98d8911ee12",
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
  "content_id": "16f6cb34-ac7d-4254-a1fe-a17a535cdffc",
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
  "content_id": "15df94cd-bd95-44e8-8f0e-4f3605f228b5",
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
  "content_id": "b30fedc1-1342-49fb-ae1e-07c875888fa9",
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
  "content_id": "a3b8ff2d-6949-47f1-a905-920df5865382",
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
  "content_id": "b8e9edf2-39be-4b16-9591-cf20b0f0acfb",
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
  "content_id": "8c363292-06d8-4efd-926e-480a262840a8",
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
  "content_id": "bd8fed42-b03a-4048-b9de-2afcd8cd3639",
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
  "content_id": "ea12dbd6-4685-4fb7-afde-8d232e3c6d03",
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
  "content_id": "e75f4683-18ea-4749-8345-07d4517a5318",
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
  "content_id": "28dedbf4-8c30-4a13-acdd-bf77e3d204c8",
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
  "content_id": "896d9ed6-4c2c-425c-b619-f7dcec40123d",
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
  "content_id": "17fd1ca4-3f0f-40a4-b507-f47bb3cfe323",
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
  "content_id": "5489757e-4cf5-4aca-8a93-0872cdc32f33",
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
  "content_id": "16b885b9-b598-45c0-8f9d-39136d9f5153",
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
  "content_id": "202487f3-6ab4-44d4-88d0-dbdb5cd4ef7b",
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
  "content_id": "6047754d-96b1-41aa-921f-001aff6ee09e",
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
  "content_id": "fafb3631-694d-41d6-833a-fa5cd4234493",
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
  "content_id": "fd5888b2-54c5-46e0-98f8-bd3eccc7d514",
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
  "content_id": "ba0582c3-b14b-484f-8bd2-2574baa2324d",
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
  "content_id": "4ab17026-ea34-4f5c-804c-29abf5071260",
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
  "content_id": "04d39eb0-a7d0-4209-8351-20c9b895e437",
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
