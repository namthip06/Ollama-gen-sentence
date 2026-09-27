# ollama-gen-sentence

Generate synthetic Thai social-media sentences with a local Ollama model, for training a content-classification model.

Sentences follow the labeling rules in [`category.md`](category.md) and are produced as JSONL (`{text, category}`) — one row per generated post — ready to feed into a classifier training pipeline.

> [!WARNING]
> This tool intentionally covers only 15 of the 18 categories in the labeling guide. Categories 8 (Hate Speech), 9 (Royal Institution), and 18 (Child Sexual Content) are **excluded by design** — the generator will refuse them.

## How it works

`generate.py` runs an interactive flow:

1. Lists models available on your machine via `ollama list`
2. Pick a category (or `a` for all 15)
3. Set sentence count, parallel request count, and output file
4. Generate in parallel batches (10 sentences per prompt) — each batch uses a different style seed for diversity
5. Rows are appended to the output JSONL

GPU-only is enforced per request (`num_gpu` forced to all layers); if Ollama reports the model running on CPU, you are asked before continuing.

## Requirements

- [Ollama](https://ollama.com) running locally with at least one Thai-capable model pulled, e.g.
  ```bash
  ollama pull qwen2.5:7b
  ```
- Python 3.12 (no third-party dependencies — stdlib only)
- A GPU for the GPU-only mode

## Setup

```bash
uv venv --python 3.12
source .venv/bin/activate.fish   # or activate for your shell
```

## Usage

```bash
uv run generate.py          # interactive mode
uv run generate.py --check  # self-check: categories, prompt template, Ollama connectivity
```

Example session:

```
โมเดลในเครื่อง:
  1. qwen2.5:7b
เลือกโมเดล: 1

หมวดที่สร้างได้:
   1. [1] Gambling (พนัน)
   ...
   a. ทุกหมวด
เลือกหมวด (เลขลำดับ หรือ a): 1
จำนวนประโยคต่อหมวด [20]: 10
จำนวน parallel request [2]:
ไฟล์ output [data/synthetic.jsonl]:
```

Output (`data/synthetic.jsonl`):

```json
{"text": "เว็บบาคาร่าออนไลน์เว็บตรง โบนัสเปิดบัญชี 50% ฝากถอนออโต้ ลิงก์ในไบโอ 🎰", "category": "1"}
```

## Project layout

| File | Purpose |
|---|---|
| `generate.py` | Interactive generator (menus, Ollama calls, JSONL output) |
| `categories.json` | Per-category definitions: rules, example sentences, style hints |
| `prompts.txt` | Prompt template with `{category_name}`, `{rules}`, `{examples}`, `{seed}`, `{n}` placeholders |
| `category.md` | Original labeling guide (reference only — edit to re-derive categories) |
| `SPEC.md` | Project specification |
| `tasks/` | Implementation plan and task list |

To adjust generation quality, edit `prompts.txt` (the prompt wording) or `categories.json` (the rules and style hints per category) — no code changes needed.
