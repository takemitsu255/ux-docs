# colima 起動

```
colima start 
```

# ビルド

```
docker-compose build
```

# 実行（1回きりのバッチとして）

```
docker-compose run --rm auto-screenshot
```

# 使い方
<p>`data.json`に対象のURLを登録する。</p>

```
    "1":{"url":"https://www.google.com/?hl=ja"},
    "2":{"url":"https://example.com/image1.png"}
```

スクリーショットは`output`に出力されます。
