from db.dbconnection import DBConnection
from data_pipeline.fetching import fetch_all_htmls
from data_pipeline.parsing import parse_all_htmls, info_parser
import asyncio
from typing import List, Tuple
from utils import get_batches
import time
import random

SLEEPTIME = 10

class InfoHandler:

    def __init__(self, dbconnection: DBConnection) -> None:
        if not isinstance(dbconnection, DBConnection):
            raise ValueError("dbconnection should be an instance of DBConnection")
        self.dbconnection = dbconnection

    def run(self, batch_size: int) -> None:
        if not isinstance(batch_size, int) or batch_size <= 0:
            raise ValueError("batch_size should be a positive integer")
        urls_info = self.dbconnection.get_distinct_urls()
        for idx, batch_range in enumerate(get_batches(0, len(urls_info), batch_size)):
            batch = urls_info[batch_range[0]:batch_range[1]+1]
            self.run_batch(batch)
            print("sleeping")
            time.sleep(random.randint(1, SLEEPTIME+1)) # throttling
            if idx % 15 == 0 and idx:
                print("sleeping for ~2minutes")
                time.sleep(random.randint(100, 120))
            if idx % 50 == 0 and idx:
                print("sleeping for ~5minutes")
                time.sleep(random.randint(300, 320))

    def run_batch(self, batch: List[Tuple]) -> None:
        urls, idxs = zip(*batch)
        htmls = asyncio.run(fetch_all_htmls(urls))
        info = parse_all_htmls(info_parser, htmls, idxs)
        self.dbconnection.add_offers(info)
        ... # add images implementation
        