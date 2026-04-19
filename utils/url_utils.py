from urllib.parse import urlparse, urljoin, parse_qs

def is_same_domain(base, url):
    return urlparse(base).netloc == urlparse(url).netloc

def normalize_url(url):
    return url.rstrip("/")

def has_params(url):
    return bool(parse_qs(urlparse(url).query))

def join_url(base, link):
    return urljoin(base, link)