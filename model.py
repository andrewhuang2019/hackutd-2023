# model.py

import pandas as pd
import statistics
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
        self.model_average = []
        self.model_error_average = []
        self.saved_sensor_data = []
        self.saved_weather_data = []
        
        
    # reads the input files and stores them in global variables
    def read_file(self):

        self.file_name1 = "leak_locations_and_rate.csv"
        self.file_name2 = "sensor_readings.csv"
        self.file_name3 = "weather_data.csv"
    
    # creates the model and returns the outcomes of the model with the input files
    def create_model_outcomes(self):
        
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
            for row_sensor in range(len(sensor_list)):
                if leak_list[row_leak][11] == sensor_list[row_sensor][1]:
                    self.saved_sensor_data.append(sensor_list[row_sensor])
                
        
        
        data_frame1 = pd.DataFrame(leak_list, columns=['EventID', 'NumberSourcesLeaking', 'LeakPointID', 'Latitude', 'Longitude', 'EmissionCategory', 'UTCStart', 'UTCEnd', 'Duration', 'LeakRate', 'BFT', 'tStart', 'tEnd'])
        print(data_frame1)

        data_frame1 = data_frame1[1:].reset_index(drop=True)
        
        data_frame2 = pd.DataFrame(self.saved_sensor_data, columns=['','time', '111111_ 40.595561_-105.14055_3', '111111_ 40.596108_-105.140583_4', '111111_40.595556_-105.140069_2', '111111_40.596114_-105.140075_1', 
                                                                    '222222_ 40.596108_-105.140583_4', '222222_40.595556_-105.140069_2', '222222_40.595561_-105.14055_3', '222222_40.596114_-105.140075_1', 
                                                                    '333333_40.595658_-105.139869_2', '333333_40.595725_-105.140008_3', '333333_40.595881_-105.139686_1', '333333_40.595947_-105.139833_4', 
                                                                    '444444_40.595658_-105.139869_2', '444444_40.595725_-105.140008_3', '444444_40.595881_-105.139686_1', '444444_40.595947_-105.139833_4', 
                                                                    '555555_40.595542_-105.139211_2', '555555_40.595547_-105.139714_3', '555555_40.596089_-105.139144_1', '555555_40.596097_-105.139678_4', 
                                                                    '666666_40.595542_-105.139211_2', '666666_40.595547_-105.139714_3', '666666_40.596089_-105.139144_1', '666666_40.596097_-105.139678_4'])
        
        print(data_frame2)
        combined_data = pd.concat([data_frame1, data_frame2], axis=1)
        
        print(combined_data)
        combined_data.fillna(0, inplace=True)
        
        columns = [combined_data['111111_ 40.595561_-105.14055_3'], combined_data['111111_ 40.596108_-105.140583_4'], combined_data['111111_40.595556_-105.140069_2'], combined_data['111111_40.596114_-105.140075_1'], 
                   combined_data['222222_ 40.596108_-105.140583_4'], combined_data['222222_40.595556_-105.140069_2'], combined_data['222222_40.595561_-105.14055_3'], combined_data['222222_40.596114_-105.140075_1'], 
                   combined_data['333333_40.595658_-105.139869_2'], combined_data['333333_40.595725_-105.140008_3'], combined_data['333333_40.595881_-105.139686_1'], combined_data['333333_40.595947_-105.139833_4'], 
                   combined_data['444444_40.595658_-105.139869_2'], combined_data['444444_40.595725_-105.140008_3'], combined_data['444444_40.595881_-105.139686_1'], combined_data['444444_40.595947_-105.139833_4'], 
                   combined_data['555555_40.595542_-105.139211_2'], combined_data['555555_40.595547_-105.139714_3'], combined_data['555555_40.596089_-105.139144_1'], combined_data['555555_40.596097_-105.139678_4'], 
                   combined_data['666666_40.595542_-105.139211_2'], combined_data['666666_40.595547_-105.139714_3'], combined_data['666666_40.596089_-105.139144_1'], combined_data['666666_40.596097_-105.139678_4']]
        
        column = combined_data['111111_ 40.596108_-105.140583_4']
        
        features = ['Duration','NumberSourcesLeaking', 'LeakRate']
        
        
        featured_data = data_frame1[features]
        featured_data.fillna(0, inplace=True)
        column.fillna(0, inplace=True)
        
        
        for index in range(len(columns)):
            train_X, val_X, train_y, val_y = train_test_split(featured_data, columns[index], random_state = 0)
            sensor_model = HistGradientBoostingRegressor(random_state=1)
            sensor_model.fit(train_X, train_y)
            prediction = sensor_model.predict(val_X)
            mean = statistics.mean(prediction)
            self.model_average.append(mean)
            mae = mean_absolute_error(val_y, prediction)
            self.model_error_average.append(mae)
            print("mean: ", mean)
            print("mae: ", mae)
            
        final_mean = statistics.mean(self.model_average)
        final_error = statistics.mean(self.model_error_average)
        
        print("Threshold For Leak: ", final_mean - (final_error / 2))
        