
from abc import ABCMeta, abstractmethod

class BaseLearningModel(metaclass=ABCMeta):
    def __init__(self, target_column: str = 'isFraud'):        
        self.target_column = target_column
        self.model = None        

    @abstractmethod
    def get_model(self):
        pass    