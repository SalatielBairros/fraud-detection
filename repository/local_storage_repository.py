import pandas as pd
from os import path, mkdir

class LocalStorageRepository:
    def __init__(self):
        self.processed_file_path = './data/processed/fraud_dataset_example_processed.csv'
        self.balanced_file_path = './data/augmented/fraud_dataset_balanced.csv'
        self.validation_file_path = './data/augmented/fraud_dataset_validation.csv'
        self.__create_directories__()
        pass

    def get_original_data(self):
        return pd.read_csv('./data/original/fraud_dataset_example.csv')

    def save_processed_data(self, dataset: pd.DataFrame):
        dataset.to_csv(self.processed_file_path, index=False)

    def save_validation_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.validation_file_path, index=False)

    def save_to_augment_data(self, dataset: pd.DataFrame):
        dataset.to_csv('./data/augmented/fraud_dataset_to_augment.csv', index=False)

    def save_balanced_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.balanced_file_path, index=False)

    def load_balanced_dataset(self):
        if(path.exists(self.balanced_file_path) and path.exists(self.validation_file_path)):
            return pd.read_csv(self.balanced_file_path)
        return None

    def load_processed_data(self):
        if(path.exists(self.processed_file_path)):
            return pd.read_csv(self.processed_file_path)
        return None

    def load_validation_dataset(self):
        return pd.read_csv(self.validation_file_path)

    def __create_directories__(self):
        if(not path.exists('./data')):
            mkdir('./data')
        if(not path.exists('./data/original')):
            mkdir('./data/original')
        if(not path.exists('./data/processed')):
            mkdir('./data/processed')
        if(not path.exists('./data/augmented')):
            mkdir('./data/augmented')