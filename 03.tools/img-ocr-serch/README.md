# colima 起動

```
colima start 
```

# ビルド

```
docker-compose build
```

# マウント変更
docker-compose.yml

`./docs`を対象のディレクトリに変更する

```
    volumes:
      - ./docs:/data:ro
      - ./output:/output
      - ./ocr_config.json:/app/ocr_config.json:ro
```

# 実行（1回きりのバッチとして）

```
docker-compose run --rm img-ocr-search
```