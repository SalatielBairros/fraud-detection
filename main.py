from fastapi import FastAPI
from environment.env_configuration import prepare_environment
from api.controllers.index_controller import router as index_router
from api.controllers.logistic_regression_controller import router as logistic_router
import os

prepare_environment()
app = FastAPI(root_path=os.environ.get('ROOT_PATH'))
app.include_router(index_router)
app.include_router(logistic_router)