import logging
from os import environ as env, path
from environment.constants import EnvironmentVariables
import wget

class BankCardsOperationIngestor:
    def __init__(self):
        self.base_path = env[EnvironmentVariables.local_storage_path]
        self.original_path = f'{self.base_path}/original'

    def ingest(self) -> str:
        filename = 'fraud_dataset_example.csv'
        if(self.__has_ingested_file__(filename)):
            return

        logging.info("Ingesting data...")
        return wget.download(f'https://caelum-online-public.s3.amazonaws.com/2423-modelos-preditivos-dados/01/{filename}', self.original_path)        

    def __has_ingested_file__(self, filename: str):
        return path.exists(f'{self.original_path}/{filename}')   
