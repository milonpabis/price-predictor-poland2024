# migrating script for PostgreSQL to Neon Cloud Service
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dbinit import Urls, Offers
from __init__ import *


if NEON_CONNECTION_URI is None:
    raise ValueError("NEON_CONNECTION_URI must be set")
engine_neon = create_engine(NEON_CONNECTION_URI)
engine_local = create_engine(LOCAL_CONNECTION_URI)

TABLES = ["urls", "offers"]

for table_name in TABLES:
    with sessionmaker(bind=engine_local)() as session_local:
        result = session_local.execute(text(f"SELECT * FROM {table_name}"))
        fetched_data = result.fetchall()

        with sessionmaker(bind=engine_neon)() as session_neon:
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
                session_neon.add_all(data, )
                session_neon.commit()

            except Exception as exception:
                print(exception)
                session_neon.rollback()
                ...
        
                








