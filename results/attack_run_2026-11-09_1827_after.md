# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:27
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `4999c594-86bb-4c6e-92b3-5a8ba4d78326` | unsure | 0.382 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `b07db8ab-a57f-4fcc-af2d-a1a2b266082f` | unsure | 0.478 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0b80ce4b-b686-4db3-9b41-37b6a6bdc147` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f18ac46d-51c0-44b4-9905-b7324ff6e91f` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f6d7a2d7-9e69-48f7-a921-eee3e222b5b8` | unsure | 0.369 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `81fde3fe-5680-41e2-83fb-40fdb8720f37` | unsure | 0.474 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `3393eb88-b07c-49fc-a67d-adea87819016` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `83e8f635-d650-4926-af62-cede566bf971` | unsure | 0.357 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `896837d4-64f3-4dd8-b0f2-55791a6facfb` | unsure | 0.602 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `9dcaa864-9a41-48ad-b58e-51084d4a27de` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `daf7df7d-7a60-443d-b7dc-49ca2f1badea` | unsure | 0.583 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `79a839df-8bc7-4670-ac4a-18f1b6ea2da7` | ai | 0.683 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `9ea4f5fb-b48c-46d5-b2a9-522c157f9cbf` | ai | 0.700 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `cb9bdde3-000c-4e7a-b6d2-b5aa9ce883d2` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `a88151ba-8ff0-4222-9e80-60e7f254e4eb` | ai | 0.718 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `68663c70-f9fd-49db-a90f-455a0b390d12` | ai | 0.699 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `4a6d7b69-e70a-4a76-a042-cdac822562d1` | ai | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `3f388c2a-ae6a-4630-b6ce-2c9bd2cf08dd` | human | 0.283 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `dd9c6e2d-c317-42c0-8b00-d426a4392ff1` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0e76f223-d65c-4b14-acdf-37f6b475cd4a` | human | 0.293 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `dae2b367-804c-47d9-802f-50fa09cecf6f` | unsure | 0.566 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `25be3069-38ac-4133-a95b-1108a1b2a97e` | unsure | 0.510 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `0073e249-c0b6-45b7-8aa4-7cf059c46105` | unsure | 0.510 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `3e5ff5db-b915-4f23-9874-9918d698d2e6` | unsure | 0.556 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `757915ee-b926-49f0-a061-8048604ee8b4` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `a59576ca-53b8-4ef1-8339-d8e57b15b4b4` | human | 0.339 |  |
| MF05 | malformed | text is a very long single word | 200 | `fc7fbe9d-f36e-487e-beb4-36da9d077574` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `f48f6604-4801-48df-8746-8872319121be` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `c6f4a489-53d0-4d90-8959-184420e7a109` | ai | 0.937 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `29e6cee1-8164-4c81-b343-9cc55d1aa5ab` | ai | 0.890 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `8c028a9e-cb97-408d-8bd5-e1c4066315f9` | unsure | 0.423 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `19c00d9d-a5f4-4949-8119-dad6d9fd4e35` | human | 0.265 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b6d724ba-630c-4f06-9d22-66c392d828af` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `02b908d1-c992-4b30-91eb-0482350518ce` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `496c2f5f-3a73-4063-9e87-9ca9ce60a480` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3e166763-1b10-4fbd-a677-0fc048007845` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `36054602-5e3a-4f3f-aafd-8d9068b28213` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `066e7e45-6d9e-431f-b6c5-e66f20c65d65` | human | 0.317 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b8a51130-01c6-402d-852b-4b039b116a26` | human | 0.317 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `253f7678-6188-42bb-9a12-3c378b9ae060` | human | 0.317 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `44ed23e6-e994-4991-8d3e-39d0fbb02e07` | human | 0.317 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f55bcf49-8b9c-44b4-991a-069bf67e6790` | human | 0.317 |  |
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
  "content_id": "4999c594-86bb-4c6e-92b3-5a8ba4d78326",
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
  "content_id": "b07db8ab-a57f-4fcc-af2d-a1a2b266082f",
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
  "content_id": "0b80ce4b-b686-4db3-9b41-37b6a6bdc147",
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
  "content_id": "f18ac46d-51c0-44b4-9905-b7324ff6e91f",
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
  "content_id": "f6d7a2d7-9e69-48f7-a921-eee3e222b5b8",
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
  "content_id": "81fde3fe-5680-41e2-83fb-40fdb8720f37",
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
  "content_id": "3393eb88-b07c-49fc-a67d-adea87819016",
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
  "content_id": "83e8f635-d650-4926-af62-cede566bf971",
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
  "content_id": "896837d4-64f3-4dd8-b0f2-55791a6facfb",
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
  "content_id": "9dcaa864-9a41-48ad-b58e-51084d4a27de",
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
  "content_id": "daf7df7d-7a60-443d-b7dc-49ca2f1badea",
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
  "content_id": "79a839df-8bc7-4670-ac4a-18f1b6ea2da7",
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
  "content_id": "9ea4f5fb-b48c-46d5-b2a9-522c157f9cbf",
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
  "content_id": "cb9bdde3-000c-4e7a-b6d2-b5aa9ce883d2",
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
  "content_id": "a88151ba-8ff0-4222-9e80-60e7f254e4eb",
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
  "content_id": "68663c70-f9fd-49db-a90f-455a0b390d12",
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
  "content_id": "4a6d7b69-e70a-4a76-a042-cdac822562d1",
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
  "content_id": "3f388c2a-ae6a-4630-b6ce-2c9bd2cf08dd",
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
  "content_id": "dd9c6e2d-c317-42c0-8b00-d426a4392ff1",
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
  "content_id": "0e76f223-d65c-4b14-acdf-37f6b475cd4a",
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
  "content_id": "dae2b367-804c-47d9-802f-50fa09cecf6f",
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
  "content_id": "25be3069-38ac-4133-a95b-1108a1b2a97e",
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
  "content_id": "0073e249-c0b6-45b7-8aa4-7cf059c46105",
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
  "content_id": "3e5ff5db-b915-4f23-9874-9918d698d2e6",
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
  "content_id": "757915ee-b926-49f0-a061-8048604ee8b4",
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
  "content_id": "a59576ca-53b8-4ef1-8339-d8e57b15b4b4",
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
  "content_id": "fc7fbe9d-f36e-487e-beb4-36da9d077574",
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
  "content_id": "f48f6604-4801-48df-8746-8872319121be",
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
  "content_id": "c6f4a489-53d0-4d90-8959-184420e7a109",
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
  "content_id": "29e6cee1-8164-4c81-b343-9cc55d1aa5ab",
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
  "content_id": "8c028a9e-cb97-408d-8bd5-e1c4066315f9",
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
  "content_id": "19c00d9d-a5f4-4949-8119-dad6d9fd4e35",
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
  "content_id": "b6d724ba-630c-4f06-9d22-66c392d828af",
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
  "content_id": "02b908d1-c992-4b30-91eb-0482350518ce",
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
  "content_id": "496c2f5f-3a73-4063-9e87-9ca9ce60a480",
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
  "content_id": "3e166763-1b10-4fbd-a677-0fc048007845",
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
  "content_id": "36054602-5e3a-4f3f-aafd-8d9068b28213",
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
  "content_id": "066e7e45-6d9e-431f-b6c5-e66f20c65d65",
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
  "content_id": "b8a51130-01c6-402d-852b-4b039b116a26",
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
  "content_id": "253f7678-6188-42bb-9a12-3c378b9ae060",
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
  "content_id": "44ed23e6-e994-4991-8d3e-39d0fbb02e07",
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
  "content_id": "f55bcf49-8b9c-44b4-991a-069bf67e6790",
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
