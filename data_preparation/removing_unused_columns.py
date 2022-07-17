import pandas as pd

class RemovingUnusedColumns:
    """
    Removing unused columns from the dataset.
    """
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self) -> pd.DataFrame:
        unique_columns = ['nameOrig', 'nameDest']
        for column in self.dataset.columns:
            if self.dataset[column].nunique() == 1:
                unique_columns.append(column)
        self.dataset = self.dataset.drop(columns=unique_columns)
        return self.dataset
