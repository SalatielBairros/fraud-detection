import pandas as pd

class ReorderingColumns:
    """
    Reorder columns to help analysis
    """
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self) -> pd.DataFrame:
        self.dataset = self.dataset[['isFraud',
            'isFlaggedFraud', 'step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
            'nameDest', 'oldbalanceDest', 'newbalanceDest']]
        return self.dataset
