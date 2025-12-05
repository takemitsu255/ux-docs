import json
import requests
import time
from playwright.sync_api import sync_playwright


def take_full_screenshot(page, url, path):
    page.goto(url, wait_until="networkidle")
    time.sleep(2)  # JS描画安定のため

# main処理
if __name__ == "__main__":
    
    print("Start Auto Screenshot Tool")

    path = "/output"

    with open('data.json', 'r') as f:
        data = json.load(f)

    for key, value in data.items():
        url = value['url']
        print(f"Processing {key}: {url}")

        # ここにスクリーンショットを撮る処理を追加する
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            context = browser.new_context()
            page = context.new_page()

            page.goto(url, wait_until="networkidle")
            time.sleep(2)  # JS描画安定のため
            page.screenshot(path=f"{path}/{key}.png", full_page=True)

            browser.close()


    print("End Auto Screenshot Tool")


    