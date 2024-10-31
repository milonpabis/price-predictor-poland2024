# from src.gui import QApplication, EntryForm

from db.dbconnection import DBConnection
from data_pipeline.fetching import fetch_all_htmls, MAIN_URI
from data_pipeline.URLHandler import URLHandler
import asyncio
import itertools
from tqdm import tqdm
from datetime import datetime

# MODEL PREDICTS THE PRICE OF A FLAT 20m2 - 80m2 IN POLAND

if __name__ == "__main__":
    # app = QApplication()
    # window = EntryForm()
    # window.show()
    # app.exec()

    # TODO:
    # - collecting every record and then saving it to the database
    # - try to find a way to iterate only on new listings
    # - separate http request from parsing
    # - parsing on separated threads


    db = DBConnection()
    url_handler = URLHandler(dbconnection=db)
    url_handler.run([1, 100], batch_size=400)
    db.close_session()

