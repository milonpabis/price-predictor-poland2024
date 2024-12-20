# from src.gui import QApplication, EntryForm

from db.dbconnection import DBConnection
from data_pipeline.fetching import fetch_all_htmls, MAIN_URI
from data_pipeline.URLHandler import URLHandler
from data_pipeline.InfoHandler import InfoHandler
from data_pipeline.parsing import url_parser
from data_pipeline.Pipelines import ExtractAndLoad, CleanAndFilter
import asyncio
import itertools
from tqdm import tqdm
from datetime import datetime
from db.__init__ import NEON_CONNECTION_URI, LOCAL_CONNECTION_URI

# MODEL PREDICTS THE PRICE OF A FLAT 20m2 - 80m2 IN POLAND

if __name__ == "__main__":
    # app = QApplication()
    # window = EntryForm()
    # window.show()
    # app.exec()

    # TODO:
    # - try to find a way to iterate only on new listings
    # - duplicates - try to implement longest subsequence in order to find duplicates on url level


    # db = DBConnection(LOCAL_CONNECTION_URI)
    # # url_handler = URLHandler(dbconnection=db)
    # # url_handler.run([1, 100], batch_size=400)
    # info_handler = InfoHandler(dbconnection=db)
    # info_handler.run(batch_size=400)

    #pipeline = ExtractAndLoad(LOCAL_CONNECTION_URI)
    #pipeline.run()

    pipeline = CleanAndFilter(LOCAL_CONNECTION_URI)
    pipeline.run()

