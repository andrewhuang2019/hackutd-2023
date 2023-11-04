# executive.py

from model import Model

class Executive:
    def __init__(self):
        pass
    
    def run(self):
        self.read_file()
        
    
    def read_file(self):
        file_name = input("Please enter a data file: ")
        data_file = open(file_name, "r")