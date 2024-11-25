# migrating script for PostgreSQL to Neon Cloud Service or in the other direction
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dbinit import Urls, Offers
from __init__ import *

TABLES = ["urls", "offers"]

def transfer_records(from_uri: str, to_uri: str, tables: list = TABLES) -> None:

    engine_from = create_engine(from_uri)
    engine_to = create_engine(to_uri)

    for table_name in tables:
        with sessionmaker(bind=engine_from)() as session_from:
            result = session_from.execute(text(f"SELECT * FROM {table_name}"))
            fetched_data = result.fetchall()

            with sessionmaker(bind=engine_to)() as session_to:
                try:
                    if table_name == "urls":
                        data = [Urls(id=idx, url=url) for idx, url in fetched_data]
                    
                    elif table_name == "offers":
                        data = [Offers(id=idx, url_id=url_idx, price=price, area=area, rooms=rooms, floor=floor, floor_num=floor_num,
                                        construction_status=construction_status, ownership=ownership, build_year=build_year,
                                        balcony=balcony, terrace=terrace, lift=lift, garage=garage, market=market, offer_type=offer_type,
                                        city=city, voivodeship=voivodeship, longitude=longitude, latitude=latitude, created_at=created_at,
                                        modified_at=modified_at) for idx, url_idx, price, area, rooms, floor, floor_num, construction_status,
                                        ownership, build_year, balcony, terrace, lift, garage, market, offer_type, city, voivodeship, longitude,
                                        latitude, created_at, modified_at in fetched_data]
                    session_to.add_all(data, )
                    session_to.commit()

                except Exception as exception:
                    print(exception)
                    session_to.rollback()
                    ...


if __name__ == "__main__":
    if NEON_CONNECTION_URI is None:
        raise ValueError("NEON_CONNECTION_URI must be set")
    transfer_records(NEON_CONNECTION_URI, LOCAL_CONNECTION_URI)
        
                








