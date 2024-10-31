from data_pipeline.fetching import fetch_all_htmls
from data_pipeline.parsing import parse_all_htmls, url_parser
from db.dbconnection import DBConnection
from utils import timelog, get_batches
import asyncio
from typing import List

class URLHandler:

    def __init__(self, dbconnection: DBConnection) -> None:
        if not isinstance(dbconnection, DBConnection):
            raise ValueError("dbconnection should be an instance of DBConnection")
        self.urls : List[str] = []
        self.dbconnection = dbconnection
    
    def run(self, idx_range: List[int], batch_size: int = 400) -> None:
        if not isinstance(idx_range, List) or len(idx_range) != 2:
            raise ValueError("idx_range should be a list of two integers")
        for batch_range in get_batches(idx_range[0], idx_range[1], batch_size):
            self.run_batch(batch_range)

    def run_batch(self, batch_idx_range: List[int]) -> None:
        urls = asyncio.run(fetch_all_htmls(batch_idx_range))
        urls = parse_all_htmls(url_parser, urls)
        self.dbconnection.add_urls(urls)




if __name__ == "__main__":
    fetcher = URLHandler()
    fetcher.run([1, 100])
    print(fetcher.urls[:10])
    print(len(fetcher.urls))