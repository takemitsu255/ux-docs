#!/usr/bin/env bash

# 使い方:
#   ./sjis_serch.sh <対象ディレクトリ> <キーワード1> [キーワード2] [出力ファイル名]
#
# 例（AND 条件）:
#   ./sjis_serch.sh . 'JQ CARD|ＪＱ　ＣＡＲＤ|JQエポス' '3倍|3P|3ポイント' result.txt
#
# 例（キーワード1だけ）:
#   ./sjis_serch.sh . 'JQ CARD|ＪＱ　ＣＡＲＤ|JQエポス'

DIR="${1:-.}"
KEY1="$2"
KEY2="$3"
OUTFILE="$4"

if [ -z "$KEY1" ]; then
  echo "Usage: $0 <dir> <keyword1> [keyword2] [output_file]" >&2
  exit 1
fi

# 出力ファイル名が指定されていなければデフォルト
if [ -z "$OUTFILE" ]; then
  OUTFILE="hit_files.txt"
fi

find "$DIR" -name '*.html' -print0 \
  | while IFS= read -r -d '' f; do
      # SJIS → UTF-8 に変換してから検索
      if nkf -w "$f" | grep -Eq -- "$KEY1"; then
        # KEY2 が空なら KEY1 だけでOK / 入っていれば AND 条件
        if [ -z "$KEY2" ] || nkf -w "$f" | grep -Eq -- "$KEY2"; then
          echo "$f"
        fi
      fi
    done \
  | sort -u > "$OUTFILE"
