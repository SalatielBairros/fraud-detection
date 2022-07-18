from sklearn.neighbors import KNeighborsClassifier
from models.base_learning_model import BaseLearningModel
import logging

class KnnModel(BaseLearningModel):
    def get_model(self) -> KNeighborsClassifier:
        if(self.model is None):
            self.model = KNeighborsClassifier()

        logging.info(f"KNeighborsClassifier model created: {self.model}")
        return self.model