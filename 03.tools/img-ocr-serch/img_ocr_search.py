#!/usr/bin/env python3
import json
from pathlib import Path

import cv2
import pytesseract

# 設定ファイル名
CONFIG_PATH = Path("ocr_config.json")


def load_config(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"設定ファイルが見つかりません: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize_ext_list(exts):
    """
    拡張子リストを正規化して set にする:
      - 先頭に . がなければ付ける
      - 小文字にする
    """
    norm = set()
    if not exts:
        return norm
    for e in exts:
        if not e:
            continue
        e = e.strip().lower()
        if not e:
            continue
        if not e.startswith("."):
            e = "." + e
        norm.add(e)
    return norm


def normalize_text(s: str) -> str:
    """
    検索しやすいように正規化：
      - 英字を小文字化
      - 空白（半角・全角・改行など）をすべて削除
    """
    return "".join(s.lower().split())


def matches(text: str, group1: list[str], group2: list[str]) -> bool:
    """
    group1: OR グループ（どれか1つ含まれれば OK）
    group2: OR グループ（どれか1つ含まれれば OK）

    判定条件:
      - group1 のいずれかを含む
      - かつ、group2 が指定されていれば、そのいずれかも含む
    """
    if not group1:
        return False

    norm_text = normalize_text(text)
    norm_group1 = [normalize_text(k) for k in group1]
    norm_group2 = [normalize_text(k) for k in group2] if group2 else []

    # group1: OR
    if not any(kw in norm_text for kw in norm_group1):
        return False

    # group2 未指定なら group1 だけで OK
    if not norm_group2:
        return True

    # group2: OR
    if not any(kw in norm_text for kw in norm_group2):
        return False

    return True


def ocr_image(path: Path, lang: str) -> str:
    """OpenCV で読み込んで前処理してから OCR する"""
    img = cv2.imread(str(path))
    if img is None:
        raise RuntimeError(f"画像を読み込めませんでした: {path}")

    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ノイズ軽減＋大津の2値化（必要に応じて調整）
    gray = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )[1]

    # OCR 実行
    text = pytesseract.image_to_string(gray, lang=lang)
    return text


def find_images(root_dir: Path, exts: set[str]):
    """対象ディレクトリ配下の画像ファイルを再帰的に列挙"""
    for p in root_dir.rglob("*"):
        if not p.is_file():
            continue
        if exts and p.suffix.lower() not in exts:
            continue
        yield p


def main():
    # 設定読み込み
    cfg = load_config(CONFIG_PATH)

    target_dir = Path(cfg.get("target_dir", "."))
    extensions = normalize_ext_list(cfg.get("extensions", []))
    keywords1 = cfg.get("keywords1", [])
    keywords2 = cfg.get("keywords2", [])
    lang = cfg.get("lang", "jpn+eng")
    output = cfg.get("output", "hit_images.txt")

    if not target_dir.exists():
        raise SystemExit(f"ターゲットディレクトリが存在しません: {target_dir}")

    if not keywords1:
        raise SystemExit("keywords1 が空です。最低1つは指定してください。（ocr_config.json）")

    if not extensions:
        print("[WARN] extensions が空です。全ファイルを対象にしてしまうので注意してください。")

    print(f"target_dir: {target_dir}")
    print(f"extensions: {sorted(extensions) if extensions else '(制限なし)'}")
    print(f"keywords1 (OR): {keywords1}")
    print(f"keywords2 (OR, AND with group1): {keywords2}")
    print(f"lang: {lang}")
    print(f"output: {output}")
    print("検索を開始します...\n")

    hit_paths: list[str] = []

    for img_path in find_images(target_dir, extensions):
        try:
            text = ocr_image(img_path, lang=lang)
        except Exception as e:
            print(f"[WARN] OCR 失敗: {img_path} ({e})")
            continue

        if matches(text, keywords1, keywords2):
            print(f"[HIT] {img_path}")
            hit_paths.append(str(img_path))

    # 結果を書き出し
    if hit_paths:
        with open(output, "w", encoding="utf-8") as f:
            for p in hit_paths:
                f.write(p + "\n")
        print(f"\n{len(hit_paths)} 件ヒットしました -> {output}")
    else:
        print("\nヒットなしでした。")


if __name__ == "__main__":
    main()
