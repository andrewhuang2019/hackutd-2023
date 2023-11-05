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
        self.saved_sensor_data = []
        self.saved_weather_data = []
        
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
        #leak_locations_data = pd.read_csv(self.file_name1)
        #sensor_readings_data = pd.read_csv(self.file_name2)
        #weather_data = pd.read_csv(self.file_name3)
        
        leak_locations_data = open(self.file_name1, "r")
        leak_list = []
        
        for line in leak_locations_data:
            line = line.strip()
            line = line.split(",")
            leak_list.append(line)
            
                
        sensor_readings_data = open(self.file_name2, "r")
        sensor_list = []
        
        for line in sensor_readings_data:
            line = line.strip()
            line = line.split(",")
            sensor_list.append(line)
            
        weather_readings_data = open(self.file_name3, "r")
        weather_list = []
        
        for line in weather_readings_data:
            line = line.strip()
            line = line.split(",")
            weather_list.append(line)            
            
        for row_leak in range(1, len(leak_list)):
            for row_sensor in range(1, len(sensor_list)):
                if leak_list[row_leak][11] == sensor_list[row_sensor][1]:
                    self.saved_sensor_data.append(sensor_list[row_sensor])
                    
        #for row_leak in range(1, len(leak_list)):
            #for row_sensor in range(1, len(weather_list)):
                #if leak_list[row_leak][6] == weather_list[row_sensor][0]:
                    #self.saved_weather_data.append(weather_list[row_sensor])
                
        print("saved_sensor_data", self.saved_sensor_data)
        #print("saved_weather_data", self.saved_weather_data)
        
        data_frame1 = pd.DataFrame(leak_list, columns= ['EventID', 'NumberSourcesLeaking', 'LeakPointID', 'Latitude', 'Longitude', 'EmissionCategory', 'UTCStart', 'UTCEnd', 'Duration', 'LeakRate', 'BFT', 'tStart', 'tEnd'])
        data_frame2 = pd.DataFrame(self.saved_sensor_data, columns=['','time', '111111_ 40.595561_-105.14055_3', '111111_ 40.596108_-105.140583_4', '111111_40.595556_-105.140069_2', '111111_40.596114_-105.140075_1', '222222_ 40.596108_-105.140583_4', '222222_40.595556_-105.140069_2', '222222_40.595561_-105.14055_3', '222222_40.596114_-105.140075_1', '333333_40.595658_-105.139869_2', '333333_40.595725_-105.140008_3', '333333_40.595881_-105.139686_1', '333333_40.595947_-105.139833_4', '444444_40.595658_-105.139869_2', '444444_40.595725_-105.140008_3', '444444_40.595881_-105.139686_1', '444444_40.595947_-105.139833_4', '555555_40.595542_-105.139211_2', '555555_40.595547_-105.139714_3', '555555_40.596089_-105.139144_1', '555555_40.596097_-105.139678_4', '666666_40.595542_-105.139211_2', '666666_40.595547_-105.139714_3', '666666_40.596089_-105.139144_1', '666666_40.596097_-105.139678_4'])
        
        combined_data = pd.concat([data_frame1, data_frame2], axis=1)
        
        columns = ['111111_ 40.595561_-105.14055_3', '111111_ 40.596108_-105.140583_4', '111111_40.595556_-105.140069_2', '111111_40.596114_-105.140075_1', '222222_ 40.596108_-105.140583_4', '222222_40.595556_-105.140069_2', '222222_40.595561_-105.14055_3', '222222_40.596114_-105.140075_1', '333333_40.595658_-105.139869_2', '333333_40.595725_-105.140008_3', '333333_40.595881_-105.139686_1', '333333_40.595947_-105.139833_4', '444444_40.595658_-105.139869_2', '444444_40.595725_-105.140008_3', '444444_40.595881_-105.139686_1', '444444_40.595947_-105.139833_4', '555555_40.595542_-105.139211_2', '555555_40.595547_-105.139714_3', '555555_40.596089_-105.139144_1', '555555_40.596097_-105.139678_4', '666666_40.595542_-105.139211_2', '666666_40.595547_-105.139714_3', '666666_40.596089_-105.139144_1', '666666_40.596097_-105.139678_4']
        
        features = ['Duration', 'NumberSourcesLeaking', 'LeakRate']
        
        featured_data = combined_data[features]
        
        for index in range(len(columns)):
            sensor_model = HistGradientBoostingRegressor(random_state=1)
            sensor_model.fit(featured_data, columns[index])
            mae = mean_absolute_error(sensor_model)
        
        #data_frame['4T-31']
        #data_frame['4T-31']
        #data_frame['4T-31']
        #data_frame['4T-31']
        #data_frame['4T-31']
        #data_frame['4T-31']
    
        '''for line in range(1, len(sensor_readings_data)):
            if int(sensor_readings_data[line][1]) == int(leak_locations_data[line][11]): #and int(sensor_readings_data[line][1]) > int(leak_locations_data[license][11]: 
                self.consolidated_data.append(sensor_readings_data[line])
                
        print(self.consolidated_data)'''

        # shuffle entire dataset
        # leak_locations_data = leak_locations_data.sample(frac = 1)

        # creates a table with only the chosen data
        """ leak_rate_column = leak_locations_data.LeakRate

        # chooses the specific features to compare data with 
        features = ['NumberSourcesLeaking', 'Latitude', 'Longitude', 'Duration'] 
        
        # creates a table with only the chosen data
        feature_data = combined_data[features]
        
        # split 20% of both rows into training data
        train_X, test_X, train_y, test_y = train_test_split(feature_data, leak_rate_column, test_size = 0.2, random_state = 1)
        
        # creates a HistGradientBoostingRegressor to creates a prediction.
        # accounts for the NaN data inside of the input file
        
        leak_locations_model = HistGradientBoostingRegressor(random_state=1)
        leak_locations_model.fit(train_X, train_y)
        
        predicted_leak_speed = leak_locations_model.predict(test_X)
        
        mae = mean_absolute_error(test_y, predicted_leak_speed)
        
        print(mae)

 """