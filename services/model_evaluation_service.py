from api.response.model_evaluation_response import ModelEvaluationResponse
import logging
from sklearn.model_selection import train_test_split
from models.base_learning_model import BaseLearningModel
from environment.constants import EnvironmentVariables
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix

class ModelEvaluationService:
    def __init__(self, model: BaseLearningModel) -> None:
        self.model = model

    def evaluate(self, train_data: pd.DataFrame) -> ModelEvaluationResponse:        
        logging.info("Evaluating model...")
        X = train_data.drop(columns=self.model.target_column)
        y = train_data[self.model.target_column]
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=EnvironmentVariables.SEED, stratify=y)
        
        model = self.model.get_model()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        accuracy = metrics.accuracy_score(y_test, y_pred)
        precision = metrics.precision_score(y_test, y_pred)
        recall = metrics.recall_score(y_test, y_pred)
        f1 = metrics.f1_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred).tolist()
        y_pred_proba = model.predict_proba(x_test)[::, 1]
        auc = metrics.roc_auc_score(y_test, y_pred_proba)

        report = metrics.classification_report(y_test, y_pred, output_dict=True,target_names=['NotFraud', 'Fraud'])
        report = {
            'Fraud': report['Fraud'],
            'NotFraud': report['NotFraud']
        }

        return ModelEvaluationResponse(
            accuracy=accuracy, 
            precision=precision, 
            recall=recall, 
            f1_score=f1,
            confusion_matrix=cm,
            roc_auc_score=auc,
            report_by_label=report)