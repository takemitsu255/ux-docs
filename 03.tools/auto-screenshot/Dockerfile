FROM python:3.10-slim

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    # libgconf-2-4 \   # ← これを削除
    libfontconfig1 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    xdg-utils \
    chromium \
    chromium-driver \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    fonts-ipafont-gothic \
    tesseract-ocr \
    libtesseract-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# 環境変数設定（chromiumのパス）
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/lib/chromium/chromedriver

# Pythonライブラリのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

# 作業ディレクトリ
WORKDIR /app

CMD ["python", "main.py"]
