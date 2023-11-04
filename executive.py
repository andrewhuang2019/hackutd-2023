# executive.py

from model import Model

class Executive:
    def __init__(self):
        self.model = None
    
    def run(self):
        self.read_file()
        
    
    def read_file(self):
        file_name = input("Please enter a data file: ")
        data_file = open(file_name, "r")
    
    def run_model(self, data_set):
        self.model = Model(data_set)
        return self.model.create_model_outcomes()