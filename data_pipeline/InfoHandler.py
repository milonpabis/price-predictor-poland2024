from db.dbconnection import DBConnection
from data_pipeline.fetching import fetch_all_htmls
from data_pipeline.parsing import parse_all_htmls, info_parser

class InfoHandler:

    def __init__(self, dbconnection: DBConnection) -> None:
        if not isinstance(dbconnection, DBConnection):
            raise ValueError("dbconnection should be an instance of DBConnection")
        self.dbconnection = dbconnection