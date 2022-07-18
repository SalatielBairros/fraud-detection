from multiprocessing.spawn import import_main_path
import pandas as pd
from sklearn.model_selection import train_test_split
from environment.constants import EnvironmentVariables
from repository.local_storage_repository import LocalStorageRepository

class SeparatingValidationData:
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.repository = LocalStorageRepository()

    def execute(self) -> pd.DataFrame:
        X = self.dataset.drop('isFraud', axis=1)
        y = self.dataset['isFraud']
        x_model, x_validation, y_model, y_validation = train_test_split(X, y, test_size=0.25, random_state = EnvironmentVariables.SEED, stratify=y)
        
        x_validation['isFraud'] = y_validation
        self.repository.save_validation_dataset(x_validation)

        x_model['isFraud'] = y_model
        self.repository.save_to_augment_data(x_model)
        return x_model
        