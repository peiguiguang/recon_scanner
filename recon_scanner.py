import argparse
from core.scheduler import start_crawl
from utils.url_utils import has_params

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-t", "--threads", type=int, default=5)
    args = parser.parse_args()

    result = start_crawl(args.url, max_depth=2, threads=args.threads)

    print("\n[+] 所有URL:")
    for url in result:
        print(url)

    print("\n[+] 含参数URL:")
    for url in result:
        if has_params(url):
            print(url)

if __name__ == "__main__":
    main()