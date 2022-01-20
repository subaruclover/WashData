"""
Form our data for APIS emulation.

Note:

1) Sample data in the simulator is based on real data but they did some small change from original data.
If we are planning to publish the result, it is better to use the data
which we can write the source in the paper.
Data which we got in OIST 19 houses could be useful.

2) Use average data of 30 mins.

The time of apis-service_center is started from 1/1 in the environment.
apis-service_center got the data from apis-web, and
the emulator or apis-web is starting from 1/1 while it is hardcoded.
For experiments, it’s better to put the data which start from 1/1 in emulator.

Create by Qiong
"""

import pandas as pd
import time
import os
from TestCSV import file_name_csv, \
                    file_name_weather, \
                    weather_split, \
                    hillside_csv,\
                    house_id_csv, \
                    house_time_csv, \
                    timeframe, \
                    timeframe_avg

start_time = time.clock()

# get current path: /Users/Huang/Documents
getpath = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
desired_dir = getpath + "/hilsideData/"
filename1 = " "
full_path1 = os.path.join(desired_dir, filename1)

raw_data_dir_2019_csv = '/Users/Huang/Documents/hilsideData/2019_csv'
# clean_data_dir_2019_csv = '/Users/Huang/Documents/hilsideDataClean/2019_csv'
clean_data_dir_2019_csv = '/Users/Huang/Documents/DQNBattery/data/2019_sift'
raw_data_dir_2019_weather = '/Users/Huang/Documents/hilsideData/2019_weather'
# clean_data_dir_2019_weather = '/Users/Huang/Documents/hilsideDataClean/2019_weather'
clean_data_dir_2019_weather = '/Users/Huang/Documents/DQNBattery/data/2019_weather'


all_weather_data_dir_2019 = r'/Users/Huang/Documents/DQNBattery/data/2019_weather'
hillside_dir_2019 = r'/Users/Huang/Documents/DQNBattery/data/2019_weather_hillside'
two_station_dir_2019_all = r'/Users/Huang/Documents/DQNBattery/data/2019_weather_2station_all'

two_station_dir_2019 = r'/Users/Huang/Documents/DQNBattery/data/2019_weather_2station'
hillside_dir_2019_overlap = r'/Users/Huang/Documents/DQNBattery/data/2019_hillside_weather'

house214_clean_data_2019 = '/Users/Huang/Documents/DQNBattery/data/house214_2019_sift_2880'

raw_data_dir_2018_csv = '/Users/Huang/Documents/hilsideData/2018_csv'
clean_data_dir_2018_csv = '/Users/Huang/Documents/DQNBattery/data/2018_sift'
# clean_data_dir_2019_csv = '/Users/Huang/Documents/DQNBattery/data/2019_sift'
raw_data_dir_2018_weather = '/Users/Huang/Documents/hilsideData/2018_weather'
clean_data_dir_2018_weather = '/Users/Huang/Documents/hilsideDataClean/2018_weather'


raw_data_dir_2017_csv = '/Users/Huang/Documents/hilsideData/2017_csv'
clean_data_dir_2017_csv = '/Users/Huang/Documents/hilsideDataClean/2017_csv'
raw_data_dir_2017_weather = '/Users/Huang/Documents/hilsideData/2017_weather'
clean_data_dir_2017_weather = '/Users/Huang/Documents/hilsideDataClean/2017_weather'

raw_data_dir_2016_csv = '/Users/Huang/Documents/hilsideData/2016_csv'
clean_data_dir_2016_csv = '/Users/Huang/Documents/hilsideDataClean/2016_csv'
raw_data_dir_2016_weather = '/Users/Huang/Documents/hilsideData/2016_weather'
clean_data_dir_2016_weather = '/Users/Huang/Documents/hilsideDataClean/2016_weather'

raw_data_dir_2015_csv = '/Users/Huang/Documents/hilsideData/2015_csv'
clean_data_dir_2015_csv = '/Users/Huang/Documents/hilsideDataClean/2015_csv'
raw_data_dir_2015_weather = '/Users/Huang/Documents/hilsideData/2015_weather'
clean_data_dir_2015_weather = '/Users/Huang/Documents/hilsideDataClean/2015_weather'

raw_data_dir_2014_csv = '/Users/Huang/Documents/hilsideData/2014_csv'
clean_data_dir_2014_csv = '/Users/Huang/Documents/hilsideDataClean/2014_csv'

# allhouse_data_dir_2019 = '/Users/Huang/Documents/hilsideDataClean/2019_csv'
# allhouse_data_dir_2019 = '/Users/Huang/Documents/DQNBattery/data/2019_csv'
allhouse_data_dir_2019 = '/Users/Huang/Documents/DQNBattery/data/2019_sift'
# onehouse_data_dir_2019 = '/Users/Huang/Documents/hilsideDataClean/2019_csv_house214'
onehouse_data_dir_2019 = '/Users/Huang/Documents/DQNBattery/data/denkishitsu_2019_sift'
# houseID = 'house214'
houseID = 'denkishitsu'

allhouse_data_dir_2018 = '/Users/Huang/Documents/DQNBattery/data/2018_sift'
# onehouse_data_dir_2019 = '/Users/Huang/Documents/hilsideDataClean/2019_csv_house214'
onehouse_data_dir_2018 = '/Users/Huang/Documents/DQNBattery/data/house214_2018_sift'
houseID = 'house214'
# houseID = 'denkishitsu'


# onehouse_data_dir_2019_May = '/Users/Huang/Documents/hilsideDataClean/2019_csv_house214_May'
onehouse_data_dir_2019_May = '/Users/Huang/Documents/DQNBattery/data/house214_2019_May'
houseID_Month = 'house214_2019'

inputfile_dir = '/Users/Huang/Documents/DQNBattery/data/house212_2019_sift'
# inputfile_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_May'
outputfile_dir = '/Users/Huang/Documents/DQNBattery/data'
outputfile_name = r'house212_2019_sift_all.csv'

inputfile_dir_2018 = '/Users/Huang/Documents/DQNBattery/data/house214_2018_sift'
# inputfile_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_May'
outputfile_dir_2018 = '/Users/Huang/Documents/DQNBattery/data'
outputfile_name_2018 = r'house214_2018_sift_all.csv'

weather_inputfile_dir = '/Users/Huang/Documents/DQNBattery/data/2019_hillside_weather'
weather_outputfile_dir = '/Users/Huang/Documents/DQNBattery/data'
weather_outputfile_name = r'hillside_2019_sift_all.csv'


raw_sample = '/Users/Huang/Documents/OES_Log_Sample/ESS/'
clean_sample = '/Users/Huang/Documents/OES_Log_Sample/sampleESS/'

if __name__ == "__main__":
    # file_name_csv(raw_data_dir_2019_csv, clean_data_dir_2019_csv)
    # file_name_csv(onehouse_data_dir_2019, house214_clean_data_2019)
    # file_name_csv(raw_data_dir_2018_csv, clean_data_dir_2018_csv)
    # file_name_csv(raw_data_dir_2017_csv, clean_data_dir_2017_csv)
    # file_name_csv(raw_data_dir_2016_csv, clean_data_dir_2016_csv)
    # file_name_csv(raw_data_dir_2015_csv, clean_data_dir_2015_csv)
    # file_name_csv(raw_data_dir_2014_csv, clean_data_dir_2014_csv)
    # file_name_weather(raw_data_dir_2019_weather, clean_data_dir_2019_weather)
    # file_name_weather(raw_data_dir_2018_weather, clean_data_dir_2018_weather)
    # file_name_weather(raw_data_dir_2017_weather, clean_data_dir_2017_weather)
    # file_name_weather(raw_data_dir_2016_weather, clean_data_dir_2016_weather)
    # file_name_weather(raw_data_dir_2015_weather, clean_data_dir_2015_weather)

    # weather_split(all_weather_data_dir_2019, hillside_dir_2019)
    # weather_split(all_weather_data_dir_2019, two_station_dir_2019_all)
    # hillside_csv(two_station_dir_2019, hillside_dir_2019_overlap)

    # house_id_csv(allhouse_data_dir_2019, onehouse_data_dir_2019, houseID)
    # house_id_csv(allhouse_data_dir_2019, onehouse_data_dir_2019_May, houseID_Month)
    # house_id_csv(allhouse_data_dir_2018, onehouse_data_dir_2018, houseID)

#######################
    # house_time_csv(inputfile_dir, outputfile_dir, outputfile_name)
    # house_time_csv(inputfile_dir_2018, outputfile_dir_2018, outputfile_name_2018)
    # house_time_csv(inputfile_dir, outputfile_dir, r'house214_2019_May.csv')

    # hillside all
    # house_time_csv(weather_inputfile_dir, weather_outputfile_dir, weather_outputfile_name)


    # timestep = 15
    # ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_sift_all.csv'
    # inputdata = pd.read_csv(ess_dir)
    # outputdata = timeframe(timestep, inputdata)
    # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_2019_quarterhour.csv', index=False)

    # average value for time window
    # timestep = 60
    # ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2018_sift_all.csv'
    # inputdata = pd.read_csv(ess_dir)
    # outputdata = timeframe_avg(timestep, inputdata)
    # # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_2018_quarterhour_avg.csv', index=False)
    # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_2018_hour_avg.csv', index=False)

    # average value for 30 mins (set for APIS input data)
    timestep = 30
    ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2018_sift_all.csv'
    inputdata = pd.read_csv(ess_dir)
    outputdata = timeframe_avg(timestep, inputdata)
    # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_2018_quarterhour_avg.csv', index=False)
    outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_2018_hour_avg.csv', index=False)

    # weather hillside
    # timestep = 15
    # ess_dir = '/Users/Huang/Documents/DQNBattery/data/hillside_2019_sift_all.csv'
    # inputdata = pd.read_csv(ess_dir)
    # outputdata = timeframe(timestep, inputdata)
    # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/hillside_2019_quarterhour.csv', index=False)

end_time = time.clock()
print("final running took %s seconds" % (end_time - start_time))

