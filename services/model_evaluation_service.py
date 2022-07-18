from api.response.model_evaluation_response import ModelEvaluationResponse
import logging
from sklearn.model_selection import train_test_split
from models.base_learning_model import BaseLearningModel
from environment.constants import EnvironmentVariables
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from repository.local_storage_repository import LocalStorageRepository

class ModelEvaluationService:
    def __init__(self, model: BaseLearningModel) -> None:
        self.model = model
        self.repository = LocalStorageRepository()

    def evaluate(self, train_data: pd.DataFrame) -> ModelEvaluationResponse:        
        logging.info("Evaluating model...")
        X = train_data.drop(columns=self.model.target_column)
        y = train_data[self.model.target_column]
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=EnvironmentVariables.SEED, stratify=y)
        
        model = self.model.get_model()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        y_pred_proba = model.predict_proba(x_test)[::, 1]
       
        return self.__get_metrics__(y_test, y_pred, y_pred_proba)

    def evaluate_augmentaded_data(self, balanced_dataset: pd.DataFrame = None) -> dict:
        if(balanced_dataset is None):
            balanced_dataset = self.repository.load_balanced_dataset()

        x_balanced = balanced_dataset.drop(columns=['isFraud']).values
        y_balanced = balanced_dataset['isFraud'].values
        x_train, x_test, y_train, y_test = train_test_split(x_balanced, y_balanced, test_size=0.15, random_state = EnvironmentVariables.SEED, stratify=y_balanced)
        
        model = self.model.get_model()
        model.fit(x_train, y_train)
        y_test_pred = model.predict(x_test)
        y_test_pred_proba = model.predict_proba(x_test)[::, 1]

        validation_dataset = self.repository.load_validation_dataset()
        x_validation = validation_dataset.drop(columns=['isFraud']).values
        y_validation = validation_dataset['isFraud'].values
        y_validation_pred = model.predict(x_validation)
        y_validation_pred_proba = model.predict_proba(x_validation)[::, 1]

        test_metrics = self.__get_metrics__(y_test, y_test_pred, y_test_pred_proba)
        validation_metrics = self.__get_metrics__(y_validation, y_validation_pred, y_validation_pred_proba)

        return {
            'test_metrics': test_metrics.dict(),
            'validation_metrics': validation_metrics.dict()
        }

    def __get_metrics__(self, y_real, y_pred, y_pred_proba) -> ModelEvaluationResponse:
        accuracy = metrics.accuracy_score(y_real, y_pred)
        precision = metrics.precision_score(y_real, y_pred)
        recall = metrics.recall_score(y_real, y_pred)
        f1 = metrics.f1_score(y_real, y_pred)
        cm = confusion_matrix(y_real, y_pred).tolist()
        auc = metrics.roc_auc_score(y_real, y_pred_proba)

        report = metrics.classification_report(y_real, y_pred, output_dict=True,target_names=['NotFraud', 'Fraud'])
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