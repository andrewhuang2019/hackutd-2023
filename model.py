# model.py

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


class Model:
    
    def __init__(self):
        self.file_name = None
        self.file_name2 = None
        self.file_name3 = None
        
    def read_file(self):
        self.file_name = input("Please enter leak locations file: ")
        #self.file_name2 = input("Please enter sensor readings file: ")
        #self.file_name3 = input("Please enter weather data file: ")
    
    def create_model_outcomes(self):
        leak_locations_data = pd.read_csv(self.file_name)
        print(leak_locations_data.columns)
        y = leak_locations_data.LeakRate
        features = ['NumberSourcesLeaking', 'Latitude', 'Longitude', 'Duration']
        X = leak_locations_data[features]
        leak_locations_model = DecisionTreeRegressor(random_state=1)
        leak_locations_model.fit(X, y)
        print(leak_locations_model.predict(X.head()))
        

