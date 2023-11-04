# model.py

class Model:
    def __init__(self, data_set):
        self.data_set = data_set
    
    def create_model_outcomes(self):
        for line in self.data_set:
            file = self.data_set.readline()
        