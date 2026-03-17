"""builds.csv → data.js に変換する。"""
import os

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, "builds.csv"), encoding="utf-8") as f:
    csv_text = f.read().strip()

with open(os.path.join(DIR, "data.js"), "w", encoding="utf-8") as f:
    f.write("const CSV = `" + csv_text + "`;")

print(f"Done: {csv_text.count(chr(10))} rows -> data.js")
