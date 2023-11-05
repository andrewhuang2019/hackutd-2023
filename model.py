# model.py

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


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

        # shuffle entire dataset
        leak_locations_data = leak_locations_data.sample(frac = 1)

        # creates a table with only the chosen data
        feature_data = leak_locations_data[features]
        leak_rate_column = leak_locations_data.LeakRate
        
        # split 20% of both rows into training data
        train_X, test_X, train_y, test_y = train_test_split.split(feature_data, leak_rate_column, test_size = 0.2, random_state = 0)

        # chooses the specific features to compare data with 
        features = ['NumberSourcesLeaking', 'Latitude', 'Longitude', 'Duration']
        
        # creates a table with only the chosen data
        feature_data = leak_locations_data[features]
        
        # creates a decision tree regressor and creates a prediction
        
        
        leak_locations_model = DecisionTreeRegressor(random_state = 0)
        leak_locations_model.fit(train_X, leak_rate_column)
        
        predicted_leak_speed = leak_locations_model.predict(test_X)
        
        print("MAE:", mean_absolute_error(leak_rate_column, predicted_leak_speed))
        
        
        
        
        max_nodes = [5, 50, 500, 5000]
        for i in max_nodes:
            
            print(self.get_mae(i, train_X, feature_data, train_y, test_y))

        
    def get_mae(self, max_leaf_nodes, train_X, val_X, train_y, val_y):
        leak_locations_model = DecisionTreeRegressor(max_leaf_nodes, random_state=1)
        leak_locations_model.fit(train_X, train_y)
        
        predicted_leak_speed = leak_locations_model.predict(val_X)
        
        mae = mean_absolute_error(val_y, predicted_leak_speed)
        
        return mae
        

