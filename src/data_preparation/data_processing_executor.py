import pandas as pd
from repository.local_storage_repository import LocalStorageRepository
from utils.data_transformation_command_handler import DataTransformationCommandHandler
from data_preparation.reordering_columns import ReorderingColumns
import logging

def execute_feature_engineering() -> pd.DataFrame:
    logging.info('Loading prepared data from local storage')
    processed_data = LocalStorageRepository().load_processed_data()

    if(processed_data is None):
        return DataTransformationCommandHandler() \
            .add_command(ReorderingColumns) \
            .execute_and_save()

    return processed_data