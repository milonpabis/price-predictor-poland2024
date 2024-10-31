from db.dbinit import Urls, Offers, create_engine, sessionmaker
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert
from typing import Iterable, List
from utils import timelog



class DBConnection:

    def __init__(self, db_name: str = "FlatsDB", password: str = "password"):
        self.engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost/{db_name}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    @timelog("Adding URLs to DB")
    def add_urls(self, urls: Iterable[str]) -> None:
        try:
            urls_dict = [{"url": url} for url in urls]
            statement = insert(Urls).values(urls_dict)
            statement = statement.on_conflict_do_nothing(index_elements=["url"]) # database will handle duplicates

            self.session.execute(statement)
            self.session.commit()
        except Exception as exception_addurl:
            print(exception_addurl)
            self.session.rollback()
            ... # close connection

    def get_distinct_urls(self) -> List[str]:
        result = self.session.execute(text("SELECT DISTINCT url FROM urls;"))
        return [row[0] for row in result]

    
    def close_session(self) -> None:
        self.session.close()

    
    def open_session(self) -> None:
        self.session = self.Session()
