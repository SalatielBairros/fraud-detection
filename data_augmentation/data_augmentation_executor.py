import pandas as pd
from repository.local_storage_repository import LocalStorageRepository
from utils.data_transformation_command_handler import DataTransformationCommandHandler
from data_augmentation.creating_fraud_data import CreatingFraudData
from data_augmentation.separating_validation_data import SeparatingValidationData
import logging

def execute_data_augmentation(processed_dataset: pd.DataFrame = None) -> pd.DataFrame:
    logging.info('Loading prepared data from local storage')
    repository = LocalStorageRepository()
    balanced_dataset = repository.load_balanced_dataset()

    if(balanced_dataset is None):
        if(processed_dataset is None):
            processed_dataset = repository.load_processed_data()
        return DataTransformationCommandHandler() \
            .add_command(SeparatingValidationData) \
            .add_command(CreatingFraudData) \
            .execute_and_save(dataset=processed_dataset)

    return balanced_dataset