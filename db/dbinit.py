from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import psycopg2

Base = declarative_base()


class Urls(Base):
    __tablename__ = "urls"

    id  = Column(Integer, primary_key=True)
    url = Column(String, nullable=False, unique=True)


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
    
    engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/FlatsDB")
    Base.metadata.create_all(engine)

