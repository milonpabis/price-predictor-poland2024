from data_pipeline.fetching import fetch_all_urls
from data_pipeline.parsing import parse_all_htmls
from db.dbconnection import DBConnection
import asyncio
from typing import List

class URLHandler:

    def __init__(self, dbconnection: DBConnection) -> None:
        self.urls : List[str] = []
        self.dbconnection = dbconnection
    
    def run(self, idx_range: List[str]) -> None:
        urls = asyncio.run(fetch_all_urls(idx_range))
        urls = parse_all_htmls(urls)
        self.dbconnection.add_urls(urls)


if __name__ == "__main__":
    fetcher = URLHandler()
    fetcher.run([1, 100])
    print(fetcher.urls[:10])
    print(len(fetcher.urls))