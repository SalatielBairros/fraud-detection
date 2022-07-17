from fastapi import APIRouter
from models.logistic_regression import LogisticRegressionModel
from services.data_service import DataService
from services.model_evaluation_service import ModelEvaluationService

router = APIRouter(prefix="/logistic")
model = LogisticRegressionModel()

@router.get("/evaluation")
def predict_text():
    data_service = DataService()
    df = data_service.load_train_data()

    lr_evaluation_service = ModelEvaluationService(LogisticRegressionModel())
    evaluation = lr_evaluation_service.evaluate(df)
    return evaluation.json()
