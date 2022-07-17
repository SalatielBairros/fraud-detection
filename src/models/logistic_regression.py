from api.response.model_evaluation_response import ModelEvaluationResponse
from sklearn.model_selection import train_test_split
from ingestion.bank_cards_data_ingestor import BankCardsOperationIngestor
import pandas as pd
from environment.constants import EnvironmentVariables
from data_preparation.data_processing_executor import execute_data_preparation
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import logging
from sklearn.metrics import confusion_matrix

class LogisticRegressionModel:
    def __init__(self, train_data: pd.DataFrame = None, target_column: str = 'isFraud'):
        self.train_data = self.__load_data__(train_data)
        self.target_column = target_column
        self.model = None
        self.model_file_path = './data/models/logistic_regression.joblib'


    def evaluate(self) -> ModelEvaluationResponse:
        logging.info("Evaluating LogisticRegression model...")
        X = self.train_data.drop(columns=self.target_column)
        y = self.train_data[self.target_column]
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=EnvironmentVariables.SEED, stratify=y)

        lr = LogisticRegression(max_iter=1000, random_state=EnvironmentVariables.SEED)
        lr.fit(x_train, y_train)
        y_pred =lr.predict(x_test)

        accuracy = metrics.accuracy_score(y_test, y_pred)
        precision = metrics.precision_score(y_test, y_pred)
        recall = metrics.recall_score(y_test, y_pred)
        f1 = metrics.f1_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred).tolist()
        y_pred_proba = lr.predict_proba(x_test)[::, 1]
        auc = metrics.roc_auc_score(y_test, y_pred_proba)

        return ModelEvaluationResponse(
            accuracy=accuracy, 
            precision=precision, 
            recall=recall, 
            f1_score=f1,
            confusion_matrix=cm,
            roc_auc_score=auc)

    def __load_data__(self, train_data: pd.DataFrame) -> pd.DataFrame:
        if(train_data is None):
            ingestor = BankCardsOperationIngestor()
            ingestor.ingest()        
            return execute_data_preparation()
        else:
            return train_data