import pandas as pd

class TypeToDummies:
    """
    This class is used to convert the type column to dummies.
    """
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self) -> pd.DataFrame:
        return pd.get_dummies(data=self.dataset, columns=['type'])
