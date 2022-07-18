from environment.constants import EnvironmentVariables
from sklearn.ensemble import RandomForestClassifier
from models.base_learning_model import BaseLearningModel
import logging

class RandomForestModel(BaseLearningModel):
    def get_model(self) -> RandomForestClassifier:
        if(self.model is None):
            self.model = RandomForestClassifier(max_depth =5, random_state=EnvironmentVariables.SEED)

        logging.info(f"RandomForestClassifier model created: {self.model}")
        return self.model