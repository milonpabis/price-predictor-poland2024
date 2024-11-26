import pandas as pd
import numpy as np



class EntryDataCleaning:
    """
    Entry pipeline, initially cleaning and preparing the data for the further processing.
    """

    def __init__(self) -> None:
        self.df = None
        self.filtered = 0

    def entry_filter(self):
        trash_rows = (self.df["price"].isna()) | (self.df["floor"].isna()) | \
                (self.df["floor_num"].isna() & self.df["construction_status"].isna() & self.df["ownership"].isna() & self.df["build_year"].isna())
        floor_filter = ~(self.df["floor"].isin(["cellar", "garret"]))
        f_arg = (~trash_rows) & floor_filter
        num_deleted = len(np.where(f_arg == False)[0]) # counting the number of deleted rows
        self.filtered += num_deleted
        self.df = self.df[f_arg] # filtering
        return self

    def extract_floors(self):
        self.df["floor"] = self.df["floor"].apply(lambda x: x.split("_")[-1] if "ground" not in x else "0")
        return self

    def extract_rooms(self):
        self.df = self.df[self.df["rooms"].str.isdigit().astype(bool)]
        return self
    
    def fill_ownership(self): # if there is NaN I read it as full_ownership
        self.df.loc[self.df["ownership"].isna(), "ownership"] = "full_ownership"
        return self

    def fill_status(self): # if build_year >= 2024 -> it's to_completion mostly
        self.df.loc[(self.df["build_year"] >= "2024") & (self.df["construction_status"].isna()), "construction_status"] = "to_completion"
        return self
    
    def cast_datatypes(self):
        self.df["price"] = self.df["price"].astype(int)
        for col in ["created_at", "modified_at"]:
            self.df[col] = pd.to_datetime(self.df[col], utc=True)
        for col in ["balcony", "terrace", "lift", "garage", "rooms", "floor"]:
            self.df[col] = self.df[col].astype(np.int8)
        for col in ["area", "latitude", "longitude"]:
            self.df[col] = self.df[col].astype(np.float64)
        for col in ["voivodeship", "city", "offer_type", "market", "ownership"]:
            self.df[col] = self.df[col].astype(str)
        for col in ["build_year", "floor_num"]:
            self.df[col] = self.df[col].astype("Int32")
        return self

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df.copy()
        self.filtered = 0
        return (
            self.entry_filter()
            .extract_floors()
            .extract_rooms()
            .fill_ownership()
            .fill_status()
            .cast_datatypes()
            .df )
