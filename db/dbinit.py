import os
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, Date, DOUBLE_PRECISION
import psycopg2
from db.__init__ import LOCAL_CONNECTION_URI

Base = declarative_base()


class Urls(Base):
    __tablename__ = "urls"

    id  = Column(Integer, primary_key=True)
    url = Column(String, nullable=False, unique=True)
    date_added = Column(Date, nullable=False)


class Offers(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey("urls.id"), nullable=False, unique=True)

    price               = Column(String, nullable=False)
    area                = Column(String, nullable=False)
    rooms               = Column(String, nullable=True)
    floor               = Column(String, nullable=True)
    floor_num           = Column(String, nullable=True)
    construction_status = Column(String, nullable=True)
    ownership           = Column(String, nullable=True)
    build_year          = Column(String, nullable=True)
    balcony             = Column(String, nullable=True)
    terrace             = Column(String, nullable=True)
    lift                = Column(String, nullable=True)
    garage              = Column(String, nullable=True)
    market              = Column(String, nullable=True)
    offer_type          = Column(String, nullable=True)
    city                = Column(String, nullable=True)
    voivodeship         = Column(String, nullable=True)
    longitude           = Column(String, nullable=False)   
    latitude            = Column(String, nullable=False)
    created_at          = Column(String, nullable=True)
    modified_at         = Column(String, nullable=True)

    url = relationship("Urls", backref="offers")


class Images(Base):
    __tablename__ = "images"

    id     = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey("offers.id"), nullable=False)
    url    = Column(String, nullable=False)


class OffersClean(Base):
    __tablename__ = "offers_clean"

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey("urls.id"), nullable=False, unique=True)

    price               = Column(Integer, nullable=False)
    area                = Column(Float, nullable=False)
    rooms               = Column(Integer, nullable=True)
    floor               = Column(Integer, nullable=True)
    floor_num           = Column(Integer, nullable=True)
    construction_status = Column(String, nullable=True)
    ownership           = Column(String, nullable=True)
    build_year          = Column(Integer, nullable=True)
    balcony             = Column(Integer, nullable=True)
    terrace             = Column(Integer, nullable=True)
    lift                = Column(Integer, nullable=True)
    garage              = Column(Integer, nullable=True)
    market              = Column(String, nullable=True)
    offer_type          = Column(String, nullable=True)
    city                = Column(String, nullable=True)
    voivodeship         = Column(String, nullable=True)
    longitude           = Column(DOUBLE_PRECISION, nullable=False)   
    latitude            = Column(DOUBLE_PRECISION, nullable=False)
    created_at          = Column(DateTime, nullable=True)
    modified_at         = Column(DateTime, nullable=True)

    url = relationship("Urls", backref="offers_clean")




def create_db(name: str = "FlatsDB") -> None:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f'CREATE DATABASE "{name}"')
    cursor.close()
    conn.close()


if __name__ == "__main__":
    try:
        create_db()
    except psycopg2.errors.DuplicateDatabase:
        print("Database already exists")
    
    # db_uri = os.environ.get("DB_URI_NEON")
    # db_password = os.environ.get("DB_PASSWORD_NEON")
    # if not db_uri or not db_password:
    #     raise ValueError("DB_URI_NEON and DB_PASSWORD_NEON environment variables must be set")
    
    engine = create_engine(LOCAL_CONNECTION_URI)
    Base.metadata.create_all(engine)

