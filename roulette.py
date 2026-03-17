import csv, random, sys, os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "builds.csv")

def load():
    with open(CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    rows = load()
    scale = None
    mood = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] in ("-s", "--scale") and i + 1 < len(args):
            scale = args[i + 1]; i += 2
        elif args[i] in ("-m", "--mood") and i + 1 < len(args):
            mood = args[i + 1]; i += 2
        elif args[i] in ("-l", "--list"):
            scales = sorted(set(r["scale"] for r in rows))
            moods = sorted(set(r["mood"] for r in rows))
            print(f"規模: {' / '.join(scales)}")
            print(f"ムード: {' / '.join(moods)}")
            print(f"全{len(rows)}件")
            return
        elif args[i] in ("-h", "--help"):
            print("使い方: python roulette.py [オプション]")
            print("  -s, --scale <規模>   規模で絞り込み (超小/小/中/大/超大)")
            print("  -m, --mood <ムード>  ムードで絞り込み")
            print("  -l, --list           選択肢と件数を表示")
            print("  -h, --help           このヘルプ")
            return
        else:
            i += 1

    filtered = rows
    if scale:
        filtered = [r for r in filtered if r["scale"] == scale]
    if mood:
        filtered = [r for r in filtered if r["mood"] == mood]

    if not filtered:
        print("該当なし。-l で選択肢を確認してね。")
        return

    b = random.choice(filtered)
    d = int(b["difficulty"])
    stars = "\u2605" * d + "\u2606" * (5 - d)
    tags = " ".join(f"#{t.strip()}" for t in b["tags"].split("|") if t.strip())

    print()
    print(f"  {b['name']}")
    print(f"  {b['category']} / {b['scale']} / {b['mood']} / {stars}")
    print()
    print(f"  {b['description']}")
    print()
    print(f"  {tags}")
    print()

if __name__ == "__main__":
    main()
