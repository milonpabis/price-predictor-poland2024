import pandas as pd
import numpy as np
from utils import timelog

class FilterOutliers:

    def __init__(self) -> None:
        self.df = None
        self.filtered = 0

    def floor_num(self):
        f_arg = (self.df["floor_num"].between(1, 17)) | (self.df["floor_num"].isna())
        num_deleted = len(np.where(f_arg == False)[0])
        self.filtered += num_deleted
        self.df = self.df[f_arg]
        return self

    def price(self):
        f_arg = self.df["price"].between(154_000, 3_000_000)
        num_deleted = len(np.where(f_arg == False)[0])
        self.filtered += num_deleted
        self.df = self.df[f_arg]
        return self

    def area(self):
        f_arg = self.df["area"].between(23, 150)
        num_deleted = len(np.where(f_arg == False)[0])
        self.filtered += num_deleted
        self.df = self.df[f_arg]
        return self

    def build_year(self):
        f_arg = (self.df["build_year"].between(1900, 2028)) | (self.df["build_year"].isna())
        num_deleted = len(np.where(f_arg == False)[0])
        self.filtered += num_deleted
        self.df = self.df[f_arg]
        return self

    @timelog("Filtering outliers")
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df.copy()
        self.filtered = 0
        return (
            self.floor_num()
            .price()
            .area()
            .build_year()
            .df
        )