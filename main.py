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

start_time = time.clock()

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
    timestep = 1  # 60
    # ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2018_sift_all.csv'
    ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_sift_all.csv'
    inputdata = pd.read_csv(ess_dir)
    outputdata = timeframe_avg(timestep, inputdata)
    # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_2018_quarterhour_avg.csv', index=False)
    outputdata = outputdata[['timestamp', 'dcdc_grid_power']]
    outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/house214_dcdc_min.csv', index=False)

    # weather hillside
    # timestep = 15
    # ess_dir = '/Users/Huang/Documents/DQNBattery/data/hillside_2019_sift_all.csv'
    # inputdata = pd.read_csv(ess_dir)
    # outputdata = timeframe(timestep, inputdata)
    # outputdata.to_csv('/Users/Huang/Documents/DQNBattery/data/hillside_2019_quarterhour.csv', index=False)

end_time = time.clock()
print("final running took %s seconds" % (end_time - start_time))

"""
import csv
import os
import time
import pandas as pd

start_time = time.time()
file = "/Users/Huang/Documents/OES_Log_Sample/ESS/F005_20190501.csv"

with open(file, 'r', encoding='UTF-8') as f:
    # 使用csv.DictReader读取文件中的信息
    reader = csv.DictReader(f)

    timestamp, charge_discharge_power, rsoc, pvc_charge_power, ups_output_power, dcdc_grid_power, p1, p2 = [], [], [], [], [], [], [], []

    for row in reader:
        timestamp.append(row['timestamp'])
        charge_discharge_power.append(row['charge_discharge_power'])
        rsoc.append(row['rsoc'])
        pvc_charge_power.append(row['pvc_charge_power'])
        ups_output_power.append(row['ups_output_power'])
        dcdc_grid_power.append(row['dcdc_grid_power'])
        p1.append(row['p1'])
        p2.append(row['p2'])


def cvs_write():
    headers = ["timestamp", "charge_discharge_power", "rsoc", "pvc_charge_power", "ups_output_power", "dcdc_grid_power",
               "p1", "p2"]
    rows = zip(
        timestamp,
        charge_discharge_power,
        rsoc,
        pvc_charge_power,
        ups_output_power,
        dcdc_grid_power,
        p1,
        p2
    )
    new_file = '/Users/Huang/Documents/OES_Log_Sample/CleanESS/F005_20190501.csv'
    with open(new_file, 'w', encoding='utf8',
              newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


if __name__ == '__main__':
    cvs_write()
print("csv.DictReader took %s seconds" % (time.time() - start_time))
"""
#
"""
with open(r'/Users/Huang/Documents/OES_Log_Sample/ESS/F004_20190501.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    timestamp, charge_discharge_power, rsoc, pvc_charge_power, ups_output_power, dcdc_grid_power, p1, p2 = [], [], [], [], [], [], [], []
    for row in reader:
        # TODO
        timestamp.append(row['timestamp'])
        charge_discharge_power.append(row['charge_discharge_power'])
        rsoc.append(row['rsoc'])
        pvc_charge_power.append(row['pvc_charge_power'])
        ups_output_power.append(row['ups_output_power'])
        dcdc_grid_power.append(row['dcdc_grid_power'])
        p1.append(row['p1'])
        p2.append(row['p2'])
        # column.remove("")

path1 = "/Users/Huang/Documents/OES_Log_Sample/CleanESS/"

def MKDir():
    dirs = os.listdir(path1)
    j = 0
    for i in range(len(timestamp)):
        print(timestamp[i])
        # print(column2[i])
    file_name = path1 + "F004_20190501"
    print(file_name)
    os.mkdir(file_name)

MKDir()
"""
