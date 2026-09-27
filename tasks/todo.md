# Todo

## Task 1: categories.json (15 หมวด)
- Acceptance: JSON 15 key, แต่ละ key มี name/rules/examples/style_hints; ไม่มี 8/9/18
- Verify: `python -c "import json; d=json.load(open('categories.json')); assert len(d)==15 and not {'8','9','18'} & set(d)"`
- Files: `categories.json`
- Scope: S

## Task 2: prompts.txt template
- Acceptance: มี placeholder ครบ {category_name} {rules} {examples} {seed} {n}; `str.format` ไม่ throw เมื่อ fill ด้วยค่าตัวอย่าง
- Verify: oneliner fill ทดสอบ
- Files: `prompts.txt`
- Scope: XS
- Depends: Task 1 (ใช้ field ชื่อเดียวกัน)

## Task 3: generate.py interactive + parallel + GPU
- Acceptance: flow ครบ 6 inputs ตาม SPEC; `ollama list` → เมนู; batch 10/prompt, ThreadPool ตาม parallel; `num_gpu: 999` + เช็ค `ollama ps` หลัง request แรก; append JSONL; block 8/9/18
- Verify: `uv run generate.py` เดินจบ flow 1 หมวด n=10 ได้ 10 แถว
- Files: `generate.py`
- Scope: S
- Depends: Task 1, 2

## Task 4: --check self-check
- Acceptance: `--check` ตรวจ categories ครบ 15 + placeholder + ยิง Ollama 1 prompt สั้นได้ response; exit code สื่อผล
- Verify: `uv run generate.py --check` ผ่าน
- Files: `generate.py`
- Scope: XS
- Depends: Task 3

## Checkpoint: Complete
- [ ] `uv run generate.py --check` ผ่าน
- [ ] รันจริง 1 หมวด n=10 → JSONL 10 แถว `{text, category}` ตรงนิยาม
