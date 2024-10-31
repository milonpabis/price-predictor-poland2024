from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor
from typing import Set, List, Callable
from multiprocessing import cpu_count
from utils import *

@timelog("HTMLs Parsing")
def parse_all_htmls(parse_fun: Callable, htmls: List[str]) -> Set[str]:
    urls = set()

    with ProcessPoolExecutor(max_workers=cpu_count()-1) as executor: # Process because of GIL
        results = executor.map(parse_fun, htmls)

        for result in results:
            urls |= result
    return urls

def url_parser(html: str) -> Set[str]:
    soup = BeautifulSoup(html, 'html.parser')
    urls = set(MAIN_URI + a["href"] for a in soup.find_all("a") if "/pl/oferta" in a["href"] and a["href"].startswith("/pl"))
    return urls

def info_parser(html: str) -> Set[str]:
    soup = BeautifulSoup(html, 'html.parser')
    # get the stuff from info to tuple and return the tuple

