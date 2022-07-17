from fastapi import APIRouter
from models.logistic_regression import LogisticRegressionModel

router = APIRouter(prefix="/logistic")
model = LogisticRegressionModel()

@router.get("/evaluation")
def predict_text():
    return model.evaluate()
