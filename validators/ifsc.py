import pandas as pd

from .config import IFSC_CODES_PATH


class IFSC:
    __instance = None

    def __init__(self):
        if self.__instance:
            return self.__instance

        self.df = pd.read_csv(IFSC_CODES_PATH)
        self.__instance = self

    def search_ifsc(IFSC):
        try:
            ifsc_detail = self.df[self.df["IFSC"] == IFSC].to_dict("r")[0]
            return ifsc_detail

        except:
            return None
