FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Tesseract 本体 + 日本語言語データ + OpenCV ランタイム依存
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-jpn \
    tesseract-ocr-jpn-vert \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir /output
RUN pip install --no-cache-dir \
    opencv-python \
    pytesseract

COPY img_ocr_search.py ocr_config.json ./

CMD ["python", "img_ocr_search.py"]
