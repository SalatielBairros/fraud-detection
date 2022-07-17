import pandas as pd
from data_preparation.data_processing_executor import execute_data_preparation
from ingestion.bank_cards_data_ingestor import BankCardsOperationIngestor
import logging


class DataService:
    def __init__(self):
        pass

    def load_train_data(self) -> pd.DataFrame:
        logging.info("Loading train data...")
        ingestor = BankCardsOperationIngestor()
        ingestor.ingest()
        return execute_data_preparation()
