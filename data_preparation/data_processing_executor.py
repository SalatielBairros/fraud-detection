import pandas as pd
from repository.local_storage_repository import LocalStorageRepository
from data_preparation.removing_unused_columns import RemovingUnusedColumns
from utils.data_transformation_command_handler import DataTransformationCommandHandler
from data_preparation.reordering_columns import ReorderingColumns
from data_preparation.data_profile_report import GenerateDataProfileReport
from data_preparation.type_to_dummies import TypeToDummies
import logging

def execute_data_preparation() -> pd.DataFrame:
    logging.info('Loading prepared data from local storage')
    processed_data = LocalStorageRepository().load_processed_data()

    if(processed_data is None):
        return DataTransformationCommandHandler() \
            .add_command(ReorderingColumns) \
            .add_command(RemovingUnusedColumns) \
            .add_command(TypeToDummies) \
            .add_command(GenerateDataProfileReport) \
            .execute_and_save()

    return processed_data