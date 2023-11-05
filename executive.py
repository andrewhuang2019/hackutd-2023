# executive.py

from model import Model


class Executive:
    def __init__(self):
        self.model = Model()
    
    def run(self):
        self.model.gather_data()
        self.model.create_model_outcomes()
        