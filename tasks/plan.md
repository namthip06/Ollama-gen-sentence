# Implementation Plan: ollama-gen-sentence

## Overview
Interactive CLI ที่ใช้ Ollama generate ประโยคไทยแบบ synthetic เข้าข่าย (Qualifies) 15 หมวดจาก category.md → JSONL สำหรับ train classifier

## Architecture Decisions
- Prompt template (`prompts.txt`, text + `{var}` placeholder) แยกจากข้อมูลหมวด (`categories.json`) — แก้ prompt ไม่ต้องแตะข้อมูล
- stdlib only: `urllib` ยิง Ollama, `ThreadPoolExecutor` ทำ parallel, `subprocess` เรียก `ollama list`/`ollama ps`
- GPU-only ผ่าน `options: {"num_gpu": 999}` + เช็ค `ollama ps` หลัง request แรก
- Hard block หมวด 8/9/18 ที่ระดับ `categories.json` (ไม่มี key) + ตรวจซ้ำใน `pick_category`

## Task List

### Phase 1: Foundation
- [ ] Task 1: เขียน `categories.json` 15 หมวดจาก category.md (name, rules, examples, style_hints; ไม่มี 8/9/18)
- [ ] Task 2: เขียน `prompts.txt` template พร้อม placeholder ครบ 5 ตัว

### Checkpoint: Foundation
- [ ] `python -c "import json; d=json.load(open('categories.json')); assert len(d)==15"` ผ่าน
- [ ] placeholder ครบ เทียบกับ `build_prompt`

### Phase 2: Core
- [ ] Task 3: `generate.py` — interactive flow (โมเดลจาก `ollama list`, หมวด, จำนวน, parallel, output path, ยืนยัน) + `build_prompt` + `call_ollama` + parse JSON array → append JSONL, batch 10 ประโยค/prompt, ThreadPool ตาม parallel, GPU check
- [ ] Task 4: `--check` self-check mode (categories ครบ 15, Ollama ตอบ 1 prompt สั้น)

### Checkpoint: Complete
- [ ] `uv run generate.py --check` ผ่าน
- [ ] รันจริง 1 หมวด n=10 ได้ JSONL 10 แถว `{text, category}` ตรงนิยาม (สุ่มตรวจด้วยคน)

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| โมเดลตอบไม่ใช่ JSON array | Med | parse แบบทน (หา `[...]` ใน response), batch fail → ข้ามและรายงาน |
| ข้อมูลหลุดหมวดต้องห้าม | High | ไม่มี key ใน categories.json + block ใน pick_category |
| GPU ไม่พอตอน parallel สูง | Low | ให้ user ระบุ parallel เอง + เตือนจาก ollama ps |

## Open Questions
- (ไม่มี — spec อนุมัติแล้ว)
