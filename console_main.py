from environment.env_configuration import prepare_environment
from models.logistic_regression import LogisticRegressionModel
from services.data_service import DataService
from services.model_evaluation_service import ModelEvaluationService
from data_augmentation.data_augmentation_executor import execute_data_augmentation
import json

prepare_environment()

data_service = DataService()
df = data_service.load_train_data()
balanced_dataset = execute_data_augmentation(df)

lr_evaluation_service = ModelEvaluationService(LogisticRegressionModel())
evaluation = lr_evaluation_service.evaluate_augmentaded_data(balanced_dataset)

print(json.dumps(evaluation, indent=4))