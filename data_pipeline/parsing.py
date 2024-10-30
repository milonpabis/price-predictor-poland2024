from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor
from typing import List
from multiprocessing import cpu_count

MAIN_URI = "https://www.otodom.pl"

def parse_html(html: str) -> List[str]:
    soup = BeautifulSoup(html, 'html.parser')
    urls = [a["href"] for a in soup.find_all("a") if "/pl/oferta" in a["href"] and a["href"].startswith("/pl")]
    return urls

def parse_all_htmls(htmls: List[str]) -> List[str]:
    urls = []

    with ProcessPoolExecutor(max_workers=cpu_count()-1) as executor:
        results = executor.map(worker, htmls)

        for result in results:
            urls.extend(result)

    return [MAIN_URI + url for url in urls]

def worker(html: str):
    parsed_urls = parse_html(html)
    return parsed_urls
