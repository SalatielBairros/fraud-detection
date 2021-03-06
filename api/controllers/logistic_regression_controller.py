from fastapi import APIRouter
from models.logistic_regression import LogisticRegressionModel
from services.data_service import DataService
from services.model_evaluation_service import ModelEvaluationService
from data_augmentation.data_augmentation_executor import execute_data_augmentation
import json

router = APIRouter(prefix="/logistic")

@router.get("/evaluation")
def evaluate_model():
    data_service = DataService()
    df = data_service.load_train_data()

    lr_evaluation_service = ModelEvaluationService(LogisticRegressionModel())
    evaluation = lr_evaluation_service.evaluate(df)
    return evaluation

@router.get("/balanced/evaluation")
def evaluate_balanced_model():
    data_service = DataService()
    df = data_service.load_train_data()
    balanced_dataset = execute_data_augmentation(df)

    lr_evaluation_service = ModelEvaluationService(LogisticRegressionModel())
    evaluation = lr_evaluation_service.evaluate_augmentaded_data(balanced_dataset)
    return evaluation