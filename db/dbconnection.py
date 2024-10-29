from db.dbinit import Urls, Offers, create_engine, sessionmaker
from sqlalchemy import text
from typing import Iterable, List



class DBConnection:

    def __init__(self, db_name: str = "FlatsDB", password: str = "password"):
        self.engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost/{db_name}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    
    def add_urls(self, urls: Iterable[str]) -> None:
        try:
            existing_urls = self.get_distinct_urls()
            url_objects = [Urls(url=u) for u in urls if u not in existing_urls]
            self.session.add_all(url_objects)
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
