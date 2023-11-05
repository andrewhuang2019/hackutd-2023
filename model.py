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
        self.csv_input = None
        self.threshold = 0.0
        self.model_average = []
        self.model_error_average = []
        self.saved_sensor_data = []
        self.saved_weather_data = []
        self.csv_list = []
        self.output_list = []
        
        
    # reads the input files and stores them in global variables
    def gather_data(self):

        self.file_name1 = "leak_locations_and_rate.csv"
        self.file_name2 = "sensor_readings.csv"
        self.file_name3 = "weather_data.csv"
    
    # reads the input of a csv file if the user wants to use their own data
    def read_input(self):
        csv_file = input("Please enter a CSV file: ")
        self.csv_input = csv_file
        
    # creates the model and returns the outcomes of the model with the input files
    def create_model_outcomes(self):
        
        # storing the opened files for usage later
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
        
        # storing the wanted sensor data for when the leaks occurred
        for row_leak in range(1, len(leak_list)):
            for row_sensor in range(len(sensor_list)):
                if leak_list[row_leak][11] == sensor_list[row_sensor][1]:
                    self.saved_sensor_data.append(sensor_list[row_sensor])
                
        # creating the first data frame for the leak file
        data_frame1 = pd.DataFrame(leak_list, columns=['EventID', 'NumberSourcesLeaking', 'LeakPointID', 'Latitude', 'Longitude', 'EmissionCategory', 'UTCStart', 'UTCEnd', 'Duration', 'LeakRate', 'BFT', 'tStart', 'tEnd'])

        # cleaning the data frame so that there are no repeat column titles
        data_frame1 = data_frame1[1:].reset_index(drop=True)
        
        # creating the second data frame for the sensors file
        data_frame2 = pd.DataFrame(self.saved_sensor_data, columns=['','time', '111111_ 40.595561_-105.14055_3', '111111_ 40.596108_-105.140583_4', '111111_40.595556_-105.140069_2', '111111_40.596114_-105.140075_1', 
                                                                    '222222_ 40.596108_-105.140583_4', '222222_40.595556_-105.140069_2', '222222_40.595561_-105.14055_3', '222222_40.596114_-105.140075_1', 
                                                                    '333333_40.595658_-105.139869_2', '333333_40.595725_-105.140008_3', '333333_40.595881_-105.139686_1', '333333_40.595947_-105.139833_4', 
                                                                    '444444_40.595658_-105.139869_2', '444444_40.595725_-105.140008_3', '444444_40.595881_-105.139686_1', '444444_40.595947_-105.139833_4', 
                                                                    '555555_40.595542_-105.139211_2', '555555_40.595547_-105.139714_3', '555555_40.596089_-105.139144_1', '555555_40.596097_-105.139678_4', 
                                                                    '666666_40.595542_-105.139211_2', '666666_40.595547_-105.139714_3', '666666_40.596089_-105.139144_1', '666666_40.596097_-105.139678_4'])
        
        # combining the two data files together to place into model
        combined_data = pd.concat([data_frame1, data_frame2], axis=1)
        
        # filling the empty values (NaN) values inside of the data to 0
        # so that the model can use it 
        combined_data.fillna(0, inplace=True)
        
        # creating a list to individualize the sensor models
        columns = [combined_data['111111_ 40.595561_-105.14055_3'], combined_data['111111_ 40.596108_-105.140583_4'], combined_data['111111_40.595556_-105.140069_2'], combined_data['111111_40.596114_-105.140075_1'], 
                   combined_data['222222_ 40.596108_-105.140583_4'], combined_data['222222_40.595556_-105.140069_2'], combined_data['222222_40.595561_-105.14055_3'], combined_data['222222_40.596114_-105.140075_1'], 
                   combined_data['333333_40.595658_-105.139869_2'], combined_data['333333_40.595725_-105.140008_3'], combined_data['333333_40.595881_-105.139686_1'], combined_data['333333_40.595947_-105.139833_4'], 
                   combined_data['444444_40.595658_-105.139869_2'], combined_data['444444_40.595725_-105.140008_3'], combined_data['444444_40.595881_-105.139686_1'], combined_data['444444_40.595947_-105.139833_4'], 
                   combined_data['555555_40.595542_-105.139211_2'], combined_data['555555_40.595547_-105.139714_3'], combined_data['555555_40.596089_-105.139144_1'], combined_data['555555_40.596097_-105.139678_4'], 
                   combined_data['666666_40.595542_-105.139211_2'], combined_data['666666_40.595547_-105.139714_3'], combined_data['666666_40.596089_-105.139144_1'], combined_data['666666_40.596097_-105.139678_4']]
        
        # the different categories of the data that we are comparing
        # the sensor values to
        features = ['Duration','NumberSourcesLeaking', 'LeakRate']
        
        # creating a smaller data frame for only the features
        # just in case filling the empty values (if there are any somehow)
        featured_data = data_frame1[features]
        
        # creating two choices for prediction of data, if you want to input own data set
        choice = input("Will you be using your own leak locations csv file? (y/n): ")
        
        # goes through all of the sensors and averages the output when put through the model
        # takes the averages of those and subtracts the final error / 2 to create a minimum threshold
        # these numbers are more or less arbitrary
        if choice == "y":
            
            self.read_input()
            csv_frame = pd.read_csv(self.csv_input)
            
            featured_data = csv_frame[features]
            
            for index in range(len(columns)):
                
                # creates the model and fits it to the data
                sensor_model = HistGradientBoostingRegressor(random_state=1)
                sensor_model.fit(featured_data, columns[index])
                
                # creates predictions on the input data frame and calculates the average
                # adds it to the global average variable
                prediction = sensor_model.predict(featured_data)
                mean = statistics.mean(prediction)
                self.model_average.append(mean)
                
                mae = mean_absolute_error(columns[index], prediction)
                self.model_error_average.append(mae)
                
                print("Mean Prediction: ", mean)
                print("Mean Average Error: ", mae)
        
        else:
            
            for index in range(len(columns)):
                
                # creates training data by splitting the featured data
                train_X, val_X, train_y, val_y = train_test_split(featured_data, columns[index], random_state = 0)
                
                # creates the model and fits it to the data
                sensor_model = HistGradientBoostingRegressor(random_state=1)
                sensor_model.fit(train_X, train_y)
                
                # creates predictions on the input data frame and calculates the average
                # adds it to the global prediction average variable
                prediction = sensor_model.predict(val_X)
                mean = statistics.mean(prediction)
                self.model_average.append(mean)
                
                # takes the mean absolute error between the actual values and the prediciton
                # adds it to the global error average variable
                mae = mean_absolute_error(val_y, prediction)
                self.model_error_average.append(mae)
                
                
                print("Mean Prediction: ", mean)
                print("Mean Average Error: ", mae)
                
        final_mean = statistics.mean(self.model_average)
        final_error = statistics.mean(self.model_error_average)
        self.threshold = final_mean - (final_error / 2)
        print("Threshold For Leak: ", self.threshold)
        
        choice2 = input("Will you be entering a sensor readings csv? (y/n): ")
        
        if choice2 == "y":
            
            self.read_input()
            csv = open(self.csv_input, "r")
            for line in csv:
                line = line.strip()
                line = line.split(",")
                self.csv_list.append(line)
            
            for row in range(1, len(self.csv_list)):
                for col in range(1, len(self.csv_list[row])):
                    #print(self.csv_list[row][col])
                    if self.csv_list[row][col] > self.threshold:   
                        self.output_list.append(self.csv_list[row])
                        break
            print(self.output_list)
            
        else:
            print("Thank you!")
        
        
        