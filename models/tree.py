from environment.constants import EnvironmentVariables
from sklearn.tree import DecisionTreeClassifier
from models.base_learning_model import BaseLearningModel
import logging

class DecisionTreeModel(BaseLearningModel):
    def get_model(self) -> DecisionTreeClassifier:
        if(self.model is None):
            self.model = DecisionTreeClassifier(max_depth =5, random_state=EnvironmentVariables.SEED)

        logging.info(f"DecisionTreeClassifier model created: {self.model}")
        return self.model