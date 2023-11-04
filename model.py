# model.py

import pandas as pd


class Model:
    
    def __init__(self):
        self.file_name = None
        self.file_name2 = None
        self.file_name3 = None
        
    def read_file(self):
        self.file_name = input("Please enter leak locations file: ")
        self.file_name2 = input("Please enter sensor readings file: ")
        self.file_name3 = input("Please enter weather data file: ")
    
    def create_model_outcomes(self):
        leak_locations_data = pd.read_csv(self.file_name)
        leak_locations_data.describe()
        
        