import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        return r.text
    except Exception as e:
        print(f"[-] 请求失败: {url}, {e}")
        return ""