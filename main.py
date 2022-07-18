from fastapi import FastAPI
from environment.env_configuration import prepare_environment
from api.controllers.index_controller import router as index_router
from api.controllers.logistic_regression_controller import router as logistic_router
from api.controllers.knn_controller import router as knn_router

prepare_environment()
app = FastAPI()
app.include_router(index_router)
app.include_router(logistic_router)
app.include_router(knn_router)
