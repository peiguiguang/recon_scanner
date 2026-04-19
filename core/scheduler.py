from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import threading

from core.crawler import extract_links
from utils.url_utils import is_same_domain, normalize_url

visited = set()
lock = threading.Lock()

def worker(queue, base_url, max_depth):
    while not queue.empty():
        url, depth = queue.get()

        url = normalize_url(url)

        if depth > max_depth:
            queue.task_done()
            continue

        with lock:
            if url in visited:
                queue.task_done()
                continue
            visited.add(url)

        print(f"[+] 爬取: {url} (深度: {depth})")

        links = extract_links(url)

        for link in links:
            if is_same_domain(base_url, link):
                queue.put((link, depth + 1))

        queue.task_done()


def start_crawl(start_url, max_depth=2, threads=5):
    q = Queue()
    q.put((start_url, 0))

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for _ in range(threads):
            executor.submit(worker, q, start_url, max_depth)

        q.join()

    return visited