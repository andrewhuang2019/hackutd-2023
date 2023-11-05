# model.py

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor


class Model:
    
    def __init__(self):
        self.file_name1 = None
        self.file_name2 = None
        self.file_name3 = None
        
    # reads the input files and stores them in global variables
    def read_file(self):
        #self.file_name = input("Please enter leak locations file: ")
        #self.file_name2 = input("Please enter sensor readings file: ")
        #self.file_name3 = input("Please enter weather data file: ")
        
        self.file_name1 = "leak_locations_and_rate.csv"
        self.file_name2 = "sensor_readings.csv"
        self.file_name3 = "weather_data.csv"
    
    # creates the model and returns the outcomes of the model with the input files
    def create_model_outcomes(self):
        
        # saves the data from the files into a table
        leak_locations_data = pd.read_csv(self.file_name1)
        sensor_readings_data = pd.read_csv(self.file_name2)
        weather_data = pd.read_csv(self.file_name3)
        
        combined_data = pd.concat([leak_locations_data, sensor_readings_data, weather_data])
        
        print(combined_data.head().describe())

        # shuffle entire dataset
        # leak_locations_data = leak_locations_data.sample(frac = 1)

        # creates a table with only the chosen data
        leak_rate_column = leak_locations_data.LeakRate

        # chooses the specific features to compare data with 
        features = ['NumberSourcesLeaking', 'Latitude', 'Longitude', 'Duration', 'Barometric_Pressure', 'Humidity', 'Temperature', 'Wind_Direction', 'Wind_Speed']
        
        # creates a table with only the chosen data
        feature_data = combined_data[features]
        
        # split 20% of both rows into training data
        train_X, test_X, train_y, test_y = train_test_split(feature_data, leak_rate_column, test_size = 0.2, random_state = 1)
        
        # creates a decision tree regressor and creates a prediction
        
        
        #leak_locations_model = DecisionTreeRegressor(random_state = 0)
        #leak_locations_model.fit(train_X, train_y)
        
        #predicted_leak_speed = leak_locations_model.predict(test_X)
        
        #print("MAE:", mean_absolute_error(test_y, predicted_leak_speed))
        
        leak_locations_model = HistGradientBoostingRegressor(random_state=1)
        leak_locations_model.fit(train_X, train_y)
        
        predicted_leak_speed = leak_locations_model.predict(test_X)
        
        mae = mean_absolute_error(test_y, predicted_leak_speed)
        
        print(mae)

