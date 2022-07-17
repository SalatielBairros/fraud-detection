from environment.constants import EnvironmentVariables
from sklearn.linear_model import LogisticRegression
from models.base_learning_model import BaseLearningModel
import logging

class LogisticRegressionModel(BaseLearningModel):
    def get_model(self) -> LogisticRegression:
        if(self.model is None):
            self.model = LogisticRegression(max_iter=1000, random_state=EnvironmentVariables.SEED)

        logging.info(f"Logistic Regression model created: {self.model}")
        return self.model