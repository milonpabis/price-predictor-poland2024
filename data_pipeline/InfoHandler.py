from db.dbconnection import DBConnection
from data_pipeline.fetching import fetch_all_htmls2
from data_pipeline.parsing import parse_all_htmls, info_parser
import asyncio
from typing import List

class InfoHandler:

    def __init__(self, dbconnection: DBConnection) -> None:
        if not isinstance(dbconnection, DBConnection):
            raise ValueError("dbconnection should be an instance of DBConnection")
        self.dbconnection = dbconnection

    def run(self) -> None:
        urls_info = self.dbconnection.get_distinct_urls()[:2]
        urls, idxs = zip(*urls_info)
        htmls = asyncio.run(fetch_all_htmls2(urls))
        info = parse_all_htmls(info_parser, htmls, idxs)
        self.dbconnection.add_offers(info)
        print(info)
        