from db.dbconnection import DBConnection
from data_pipeline.InfoHandler import InfoHandler
from data_pipeline.URLHandler import URLHandler
from db.__init__ import NEON_CONNECTION_URI

class ExtractAndLoad:

    def __init__(self, db_uri: str = NEON_CONNECTION_URI) -> None:
        self.db = DBConnection(db_uri)
        self.url_handler = URLHandler(self.db)
        self.info_handler = InfoHandler(self.db)

    def run(self) -> None:
        self.url_handler.run([1, 2400], batch_size=400) # implement to run only on potentially new listings
        self.info_handler.run(batch_size=400)