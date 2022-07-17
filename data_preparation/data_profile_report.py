import pandas as pd
from pandas_profiling import ProfileReport
import logging
from os import path

class GenerateDataProfileReport:
    """
    Generates a data profile report for the given dataset.
    """
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.output_file_path = "./analysis/fraud_dataset_profile_report.html"

    def should_execute(self) -> bool:
        return not path.exists(self.output_file_path)

    def execute(self) -> pd.DataFrame:        
        logging.info("Generating data profile report...")
        ProfileReport(self.dataset).to_file(self.output_file_path)
        logging.info(f"Data profile report generated on {self.output_file_path}")
        return self.dataset
