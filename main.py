# from src.gui import QApplication, EntryForm

from db.dbconnection import DBConnection
from data_pipeline.fetching import fetch_all_urls, MAIN_URI
import asyncio
import itertools
from tqdm import tqdm

REQUESTS_BATCH = 100
NUM_REQUESTS = 2500
NUM_BATCHES = 2500 // REQUESTS_BATCH

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

    for i in tqdm(range(1, NUM_BATCHES+1)):
        urls = asyncio.run(fetch_all_urls([((i-1)*REQUESTS_BATCH)+1, i*REQUESTS_BATCH]))
        urls_flat = set(list(itertools.chain.from_iterable(urls)))
        urls_full = list(map(lambda ur: MAIN_URI + ur, urls_flat))

        db.add_urls(urls_full)
    
    db.close_session()
