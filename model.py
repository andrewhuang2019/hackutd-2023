# model.py

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


class Model:
    
    def __init__(self):
        self.file_name = None
        self.file_name2 = None
        self.file_name3 = None
        
    # reads the input files and stores them in global variables
    def read_file(self):
        self.file_name = input("Please enter leak locations file: ")
        #self.file_name2 = input("Please enter sensor readings file: ")
        #self.file_name3 = input("Please enter weather data file: ")
    
    # creates the model and returns the outcomes of the model with the input files
    def create_model_outcomes(self):
        
        # saves the data from the files into a table
        leak_locations_data = pd.read_csv(self.file_name)
        leak_rate_column = leak_locations_data.LeakRate
        
        # chooses the specific features to compare data with 
        features = ['NumberSourcesLeaking', 'Latitude', 'Longitude', 'Duration']
        
        # creates a table with only the chosen data
        feature_data = leak_locations_data[features]
        
        # creates a decision tree regressor and creates a prediction
        leak_locations_model = DecisionTreeRegressor(random_state=1)
        leak_locations_model.fit(feature_data, leak_rate_column)
        print(leak_locations_model.predict(feature_data.head()))
        
        predicted_leak_speed = leak_locations_model.predict(feature_data.head())
        
        mean_absolute_error(leak_rate_column, predicted_leak_speed)
        
        

