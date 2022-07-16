import pandas as pd
from os import path

class LocalStorageRepository:
    def __init__(self):
        self.processed_file_path = 'data/processed/fraud_dataset_example_processed.csv'
        pass

    def get_original_data(self):
        return pd.read_csv('data/original/fraud_dataset_example.csv')

    def save_processed_data(self, dataset: pd.DataFrame):
        dataset.to_csv('data/processed/fraud_dataset_example_processed.csv', index=False)

    def load_processed_data(self):
        if(path.exists(self.processed_file_path)):
            return pd.read_csv(self.processed_file_path)
        return None