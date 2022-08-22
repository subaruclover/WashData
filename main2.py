import pandas as pd
import time
from TestCSV import file_name_csv, \
                    file_name_weather, \
                    weather_split, \
                    hillside_csv,\
                    house_id_csv, \
                    house_time_csv, \
                    timeframe, \
                    timeframe_avg

allhouse_data_dir_2018 = '/Users/Huang/Documents/DQNBattery/data/2018_sift'
# onehouse_data_dir_2018 = '/Users/Huang/Documents/hilsideDataClean/2018_csv_house214'
onehouse_data_dir_2018 = '/Users/Huang/Documents/DQNBattery/data/house215_2018_sift'
houseID = 'house215'
# houseID = 'denkishitsu'

house_id_csv(allhouse_data_dir_2018, onehouse_data_dir_2018, houseID)