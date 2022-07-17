from environment.env_configuration import prepare_environment
from models.logistic_regression import LogisticRegressionModel
from services.data_service import DataService
from services.model_evaluation_service import ModelEvaluationService
import json

prepare_environment()

data_service = DataService()
df = data_service.load_train_data()

lr_evaluation_service = ModelEvaluationService(LogisticRegressionModel())
evaluation = lr_evaluation_service.evaluate(df)

print(evaluation.json(indent=4))