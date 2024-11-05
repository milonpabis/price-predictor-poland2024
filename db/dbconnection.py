from db.dbinit import Urls, Offers, create_engine, sessionmaker
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
from typing import Iterable, Tuple, List
from utils import *



class DBConnection:

    def __init__(self, db_name: str = "FlatsDB", password: str = "password"):
        self.engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost/{db_name}")
        self.Session = sessionmaker(bind=self.engine)

    @timelog("Adding URLs to DB")
    def add_urls(self, urls: Iterable[str]) -> None:
        with self.Session() as session:
            try:
                urls_dict = [{"url": url} for url in urls]
                statement = insert(Urls).values(urls_dict)
                statement = statement.on_conflict_do_nothing(index_elements=["url"]) # database will handle duplicates

                session.execute(statement)
                session.commit()
            except Exception as exception_addurl:
                print(exception_addurl)
                session.rollback()
                ... # close connection

    
    @timelog("Adding offers to DB")
    def add_offers(self, offers: Iterable[Tuple[str]]) -> None:
        with self.Session() as session:
            try:
                offers = [Offers(url_id=url_idx, price=price, area=area, rooms=rooms, floor=floor, floor_num=floor_num,
                                construction_status=construction_status, ownership=ownership, build_year=build_year,
                                balcony=balcony, terrace=terrace, lift=lift, garage=garage, market=market, offer_type=offer_type,
                                city=city, voivodeship=voivodeship, longitude=longitude, latitude=latitude, created_at=created_at,
                                modified_at=modified_at) for url_idx, price, area, rooms, floor, floor_num, construction_status,
                                ownership, build_year, balcony, terrace, lift, garage, market, offer_type, city, voivodeship, longitude,
                                latitude, created_at, modified_at in offers]
                session.add_all(offers, )
                session.commit()

            except Exception as exception:
                print(exception)
                session.rollback()
                ...

    def get_distinct_urls(self) -> List[str]:
        with self.Session() as session:
            result = session.execute(text(Q_GET_DISTINCT_URLS))
            return result.fetchall()
