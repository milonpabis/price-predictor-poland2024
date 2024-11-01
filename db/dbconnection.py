from db.dbinit import Urls, Offers, create_engine, sessionmaker
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert
from typing import Iterable, Tuple, List
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

    
    @timelog("Adding offers to DB")
    def add_offers(self, offers: Iterable[Tuple[str]]) -> None:
        try:
            offers = [Offers(url_id=url_idx, price=price, area=area, rooms=rooms, floor=floor, floor_num=floor_num,
                              construction_status=construction_status, ownership=ownership, build_year=build_year,
                              balcony=balcony, terrace=terrace, lift=lift, garage=garage, market=market, offer_type=offer_type,
                              city=city, voivodeship=voivodeship, longitude=longitude, latitude=latitude, created_at=created_at,
                              modified_at=modified_at) for url_idx, price, area, rooms, floor, floor_num, construction_status,
                              ownership, build_year, balcony, terrace, lift, garage, market, offer_type, city, voivodeship, longitude,
                              latitude, created_at, modified_at in offers]
            self.session.add_all(offers)
            self.session.commit()

        except Exception as exception:
            print(exception)
            self.session.rollback()
            ...

    def get_distinct_urls(self) -> List[str]:
        result = self.session.execute(text("SELECT DISTINCT url, id FROM urls;"))
        return result.fetchall()

    
    def close_session(self) -> None:
        self.session.close()

    
    def open_session(self) -> None:
        self.session = self.Session()
