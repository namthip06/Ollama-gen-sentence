# Spec: ollama-gen-sentence

## Objective
CLI tool ที่ใช้ Ollama generate ประโยคโซเชียลมีเดียภาษาไทยแบบ synthetic ที่เข้าข่าย (Qualifies) ตามนิยามหมวดใน `category.md` เพื่อใช้เป็น positive training samples ให้ content classifier

**ขอบเขตหมวด:** 15 หมวด (ข้าม 8 Hate Speech, 9 สถาบัน, 18 Child Sexual Content — 18 ห้ามสร้างเด็ดขาด)

**Success:**
- รัน `generate.py` แล้วเดิน interactive: เลือกหมวด → ใส่จำนวน → ยืนยัน → ได้ JSONL แถว `{text, category}`
- ประโยคภาษาไทย ตรงนิยาม Qualifies ของหมวด (สุ่มตรวจด้วยคน)
- ทุกหมวดใน 15 หมวด generate ได้

## Tech Stack
- Python 3.12 (venv ด้วย `uv venv`)
- stdlib only (`urllib.request` ยิง Ollama API, `concurrent.futures` ทำ parallel, `subprocess` เรียก `ollama list`/`ollama ps`) — ไม่เพิ่ม dependency
- โมเดลจาก `ollama list` ที่ user เลือก (ไม่มี default ตายตัว)

## Commands
```bash
uv venv --python 3.12 && source .venv/bin/activate.fish
uv run generate.py                  # interactive mode
uv run generate.py --check          # self-check: parse categories.json + ยิง Ollama 1 prompt สั้น
```

## Project Structure
```
generate.py      → interactive program (menu, input, call Ollama, write JSONL)
prompts.txt      → prompt template แบบ text มี var {category_name} {rules} {examples} {seed} {n}
categories.json  → รายละเอียดแต่ละหมวดเป็น JSON (จาก category.md)
category.md      → แหล่งอ้างอิงต้นฉบับ (input, แก้ไม่ได้จาก script)
data/            → synthetic.jsonl (append)
SPEC.md
```

### categories.json รูปแบบ
```json
{
  "1": {
    "name": "Gambling (พนัน)",
    "rules": "เกณฑ์ Qualifies + Does Not Qualify ย่อ",
    "examples": "ตัวอย่าง Pass จาก category.md",
    "style_hints": ["ราคาส่ง", "โบนัสสมัคร", "ลิงก์ในไบโอ"]
  }
}
```
- หมวด 8, 9, 18 ไม่มี key และ script ไม่รับ

### prompts.txt รูปแบบ
text template มี placeholder `{category_name}`, `{rules}`, `{examples}`, `{seed}`, `{n}` —
`generate.py` โหลด categories.json แล้ว fill var ลง template ด้วย `str.format`

## Code Style
ฟังก์ชันเล็ก top-level, input() แบบ interactive, ไม่มี class:
```python
def load_categories(path: str) -> dict: ...
def load_template(path: str) -> str: ...
def build_prompt(template: str, cat: dict, seed: str, n: int) -> str: ...
def call_ollama(prompt: str, model: str, parallel_hint: int) -> str: ...
def pick_category(categories: dict) -> list[str]:  # เมนูเลขหมวด / "a" = ทุกหมวด, วนจนได้ input ถูก
```

## Flow ของ generate.py (user inputs)

```
1. โหลด categories.json  (ถ้า fail → แจ้งและออก)
2. รัน `ollama list` → แสดงรายการโมเดลที่มีในเครื่อง (เลข + ชื่อ) → input เลือกโมเดล
3. เลือกหมวด        → input เลขหมวด หรือ "a" = ทุกหมวด
   แสดงเมนู "เลข. ชื่อ" 15 แถว; input ผิด/เป็นหมวดต้องห้าม → เตือนแล้วถามใหม่
4. จำนวนประโยค      → input เลข (Enter = default 20)
5. จำนวน parallel    → input เลข request พร้อมกัน (Enter = default 2)
6. ไฟล์ output      → input path (Enter = data/synthetic.jsonl)
7. สรุปยืนยัน: โมเดล / หมวด / จำนวน / parallel / ไฟล์ → input y/n (n = กลับขั้น 3)
8. generate แบบ parallel (ThreadPool, ปล่อยตามจำนวนที่ถาม; ทีละ batch 10 ประโยค/prompt,
   style สุ่มจาก style_hints, options num_gpu สูงเพื่อบังคับ layer ทั้งหมดลง GPU)
   → แสดง progress ต่อ batch → append JSONL
9. ถาม "ทำหมวดอื่นต่อไหม? (y/n)" → y = กลับขั้น 3, n = ออก (สรุปยอดรวม)
```

Inputs ทั้งหมด 6 ตัว: โมเดล, หมวด, จำนวน, parallel, ไฟล์ output, ยืนยัน (+ y/n วนต่อ)

**GPU-only:** ทุก request ส่ง `options: {"num_gpu": 999}` (บังคับ all layers on GPU); ก่อนเริ่มรัน `ollama ps` หลัง request แรก — ถ้า PROCESSOR ขึ้น CPU เตือนแล้วให้ user ยืนยันว่าจะรันต่อไหม

## Testing Strategy
ไม่มี pytest — self-check ใน `__main__`/`--check` mode:
- `--check`: `categories.json` parse ได้และมีครบ 15 หมวด, ยิง Ollama 1 prompt สั้นได้ response

## Prompt Design
ใส่ใน prompt: นิยาม + เกณฑ์ Qualifies + ตัวอย่าง Pass ของหมวดนั้น + คำสั่ง "เขียนประโยคโพสต์โซเชียลภาษาไทย n ประโยค ที่เข้าข่าย, หลากหลายรูปแบบ, ตอบเป็น JSON array" → parse JSON, แตกเป็นแถว JSONL
- สุ่ม "มุม/สไตล์" (ราคาส่ง, CTA, โปรโมชั่น ฯลฯ) ใส่ seed ใน prompt เพื่อ diversity

## Boundaries
- Always: ตรวจว่า category ที่ขออยู่ใน 15 หมวดที่อนุญาต; append ไม่ทับไฟล์เดิม
- Ask first: เพิ่ม dependency, แก้ category.md
- Never: หมวด 8, 9, 18; เขียนทับ data/synthetic.jsonl

## Not Doing
- Hard negatives / edge cases, auto-filter/self-check คุณภาพ, UI, fine-tune pipeline
