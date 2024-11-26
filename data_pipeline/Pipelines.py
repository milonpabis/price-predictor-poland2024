from db.dbconnection import DBConnection
from data_pipeline.InfoHandler import InfoHandler
from data_pipeline.URLHandler import URLHandler
from data_pipeline.EntryDataCleaning import EntryDataCleaning
from data_pipeline.FilterOutliers import FilterOutliers
from db.__init__ import LOCAL_CONNECTION_URI

class ExtractAndLoad:

    def __init__(self, db_uri: str = LOCAL_CONNECTION_URI) -> None:
        self.db = DBConnection(db_uri)
        self.url_handler = URLHandler(self.db)
        self.info_handler = InfoHandler(self.db)

    def run(self) -> None:
        self.url_handler.run([1, 2400], batch_size=400) # implement to run only on potentially new listings
        self.info_handler.run(batch_size=400)

    
class CleanAndFilter:

    def __init__(self, db_uri: str = LOCAL_CONNECTION_URI):
        self.db = DBConnection(db_uri)
        self.entry_cleaning = EntryDataCleaning()
        self.filter_outliers = FilterOutliers()
        self.df = self.db.get_raw_offers()

    def run(self) -> None:
        cleaned = self.entry_cleaning.run(self.df)
        filtered = self.filter_outliers.run(cleaned)
        self.db.add_offers_clean(filtered)
