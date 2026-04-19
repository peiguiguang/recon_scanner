from bs4 import BeautifulSoup
from core.fetcher import fetch
from utils.url_utils import join_url

def extract_links(url):
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        link = join_url(url, a["href"])

        if not link.startswith("http"):
            continue

        links.append(link)

    return links