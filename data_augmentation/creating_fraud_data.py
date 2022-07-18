import pandas as pd
from imblearn.over_sampling import ADASYN
from repository.local_storage_repository import LocalStorageRepository
from environment.constants import EnvironmentVariables

class CreatingFraudData:
    def __init__(self, to_balance_dataset: pd.DataFrame) -> None:
        self.to_balance_dataset = to_balance_dataset
        self.repository = LocalStorageRepository()

    def execute(self):
        X = self.to_balance_dataset.drop('isFraud', axis=1)
        y = self.to_balance_dataset['isFraud']
        adasyn = ADASYN(sampling_strategy=EnvironmentVariables.FraudProportion, random_state=EnvironmentVariables.SEED)
        x_resampled, y_resampled = adasyn.fit_resample(X, y)
        df_balanced = pd.concat([y_resampled, x_resampled], axis=1)
        self.repository.save_balanced_dataset(df_balanced)
        return df_balanced