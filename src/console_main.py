from environment.env_configuration import prepare_environment
from ingestion.bank_cards_data_ingestor import BankCardsOperationIngestor
from data_preparation.data_processing_executor import execute_data_preparation

prepare_environment()

ingestor = BankCardsOperationIngestor()
ingestor.ingest()

df = execute_data_preparation()