"""Interactive CLI: generate synthetic Thai social-media sentences via Ollama.

Usage:
    uv run generate.py            # interactive mode
    uv run generate.py --check    # self-check (categories, template, Ollama)
"""
import argparse
import concurrent.futures
import json
import random
import subprocess
import sys
import urllib.request
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
BASE_DIR = Path(__file__).parent
DEFAULT_OUT = "data/synthetic.jsonl"
BATCH_SIZE = 10
DEFAULT_N = 20
DEFAULT_PARALLEL = 2


def load_categories(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_prompt(template: str, cat: dict, seed: str, n: int) -> str:
    return template.format(
        category_name=cat["name"],
        rules=cat["rules"],
        examples="\n".join("- " + e for e in cat["examples"]),
        seed=seed,
        n=n,
    )


def call_ollama(prompt: str, model: str) -> str:
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"num_gpu": 999, "temperature": 0.9},
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.loads(resp.read())["response"]


def parse_sentences(response: str) -> list[str]:
    """Parse model output as JSON array of strings; tolerate ``` fences."""
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        start, end = response.find("["), response.rfind("]")
        if start == -1 or end == -1:
            return []
        try:
            data = json.loads(response[start:end + 1])
        except json.JSONDecodeError:
            return []
    if isinstance(data, dict):
        data = next((v for v in data.values() if isinstance(v, list)), [])
    return [s for s in data if isinstance(s, str) and s.strip()]


def check_gpu(model: str) -> str:
    """Return ollama ps processor line, 'CPU' if loaded on CPU."""
    try:
        out = subprocess.run(["ollama", "ps"], capture_output=True, text=True,
                             timeout=10).stdout
        for line in out.splitlines():
            if line.startswith(model.split(":")[0]):
                return line
    except (OSError, subprocess.TimeoutExpired):
        pass
    return ""


def list_models() -> list[str]:
    try:
        out = subprocess.run(["ollama", "list"], capture_output=True, text=True,
                             timeout=10).stdout
    except (OSError, subprocess.TimeoutExpired):
        sys.exit("เชื่อมต่อ Ollama ไม่ได้ — รัน 'ollama serve' ก่อน")
    models = [line.split()[0] for line in out.splitlines()[1:] if line.strip()]
    if not models:
        sys.exit("ไม่มีโมเดลในเครื่อง — ollama pull ก่อน (เช่น qwen2.5:7b)")
    return models


def ask_int(prompt: str, default: int) -> int:
    raw = input(f"{prompt} [{default}]: ").strip()
    try:
        return int(raw) if raw else default
    except ValueError:
        return default


def ask_str(prompt: str, default: str) -> str:
    raw = input(f"{prompt} [{default}]: ").strip()
    return raw or default


def pick_categories(categories: dict) -> list[str]:
    keys = sorted(categories, key=int)
    print("\nหมวดที่สร้างได้:")
    for i, k in enumerate(keys, 1):
        print(f"  {i:2d}. [{k}] {categories[k]['name']}")
    print("   a. ทุกหมวด")
    while True:
        raw = input("เลือกหมวด (เลขลำดับ หรือ a): ").strip().lower()
        if raw == "a":
            return keys
        if raw.isdigit() and 1 <= int(raw) <= len(keys):
            return [keys[int(raw) - 1]]
        print("  input ไม่ถูกต้อง ลองใหม่")


def run_category(template: str, categories: dict, cat_key: str, model: str,
                 n: int, parallel: int, out_path: Path) -> int:
    cat = categories[cat_key]
    total = 0
    batches = [min(BATCH_SIZE, n - i) for i in range(0, n, BATCH_SIZE)]

    def do_batch(size: int, attempt: int) -> list[str]:
        seed = ", ".join(random.sample(cat["style_hints"],
                                       k=min(2, len(cat["style_hints"])))) \
               + f" (รูปแบบที่ {attempt})"
        prompt = build_prompt(template, cat, seed, size)
        return parse_sentences(call_ollama(prompt, model))

    gpu_checked = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=parallel) as pool:
        futures = {pool.submit(do_batch, size, i): size
                   for i, size in enumerate(batches)}
        for fut in concurrent.futures.as_completed(futures):
            try:
                sentences = fut.result()
            except Exception as e:
                print(f"  batch ล้มเหลว: {e} — ข้าม")
                continue
            if not gpu_checked:
                ps = check_gpu(model)
                if "100% GPU" not in ps and ps:
                    if "CPU" in ps and input(
                            "โมเดลรันบน CPU! รันต่อ? (y/n): ").lower() != "y":
                        sys.exit("หยุดตามคำขอผู้ใช้")
                gpu_checked = True
            with out_path.open("a", encoding="utf-8") as f:
                for s in sentences:
                    f.write(json.dumps({"text": s, "category": cat_key},
                                       ensure_ascii=False) + "\n")
            total += len(sentences)
            print(f"  [{cat_key}] +{len(sentences)} ประโยค (รวม {total}/{n})")
    return total


def self_check() -> int:
    categories = load_categories(BASE_DIR / "categories.json")
    assert len(categories) == 15, f"expected 15 categories, got {len(categories)}"
    assert not {"8", "9", "18"} & set(categories), "forbidden category present"
    template = load_template(BASE_DIR / "prompts.txt")
    p = build_prompt(template, categories["1"], "ทดสอบ", 1)
    for var in ("Gambling", "ทดสอบ"):
        assert var in p, f"template var missing: {var}"
    print("categories.json + prompts.txt OK")
    try:
        r = call_ollama("ตอบสั้นๆ: 1+1=?", list_models()[0])
        print("Ollama OK:", r.strip()[:50])
    except SystemExit as e:
        print(f"Ollama FAIL: {e}")
        return 1
    except Exception as e:
        print(f"Ollama FAIL: {e}")
        return 1
    return 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.check:
        sys.exit(self_check())

    categories = load_categories(BASE_DIR / "categories.json")
    template = load_template(BASE_DIR / "prompts.txt")
    models = list_models()
    print("\nโมเดลในเครื่อง:")
    for i, m in enumerate(models, 1):
        print(f"  {i}. {m}")
    while True:
        raw = input("เลือกโมเดล: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(models):
            model = models[int(raw) - 1]
            break
        if raw in models:
            model = raw
            break
        print("  ไม่พบโมเดล ลองใหม่")

    grand = 0
    while True:
        keys = pick_categories(categories)
        n = ask_int("จำนวนประโยคต่อหมวด", DEFAULT_N)
        parallel = ask_int("จำนวน parallel request", DEFAULT_PARALLEL)
        out_path = Path(ask_str("ไฟล์ output", DEFAULT_OUT))

        print(f"\nสรุป: model={model} หมวด={','.join(keys)} n={n}/หมวด "
              f"parallel={parallel} out={out_path}")
        if input("เริ่ม generate? (y/n): ").strip().lower() != "y":
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        for k in keys:
            grand += run_category(template, categories, k, model, n,
                                  parallel, out_path)
        if input("ทำหมวดอื่นต่อไหม? (y/n): ").strip().lower() != "y":
            break
    print(f"\nเสร็จสิ้น รวม {grand} ประโยค")


if __name__ == "__main__":
    main()
