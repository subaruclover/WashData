import pandas as pd
import os
import re
import glob
import numpy as np
import random
import time
"""
allhouse_data_dir = '/Users/Huang/Documents/hilsideDataClean/2019_csv'
onehouse_data_dir = '/Users/Huang/Documents/hilsideDataClean/2019_csv_house215'
houseID = 'house215'

# def house_id_csv(allhouse_data_dir, onehouse_data_dir, houseID):
# allhouse_data_dir : all houses data directory
# onehouse_data_dir : targeted house clean data directory
# houseID: houseID, string type, e.g., 'house214'

os.chdir(allhouse_data_dir)  # path of original csv data files
allhouse_data_dir = os.getcwd()  # read current file path

file_list = []  # file name stored in file_list
for root, dirs, files in os.walk(allhouse_data_dir):
    for file in files:
        dirname, filename = os.path.split(file)
        # filename.split('_', 1)[0]
        if filename.split('_', 1)[0] == houseID:
        # if filename.split('05', 1)[0] == houseID:  # May
            # print(file)
            file_list.append(file)

# print(file_list)
new_path = onehouse_data_dir
for csv in file_list:
    data = pd.read_csv(csv)
    df = pd.DataFrame(data)
    # export to csv files
    df.to_csv(os.path.join(new_path, csv), index=False)
"""

# df_raw = pd.read_csv('/Users/Huang/Documents/hilsideDataClean/2019_csv_house215/house215_20190101.csv')
# df = df_raw[1:2851]
"""
raw_data_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_May'
# clean_data_dir_2019_csv = '/Users/Huang/Documents/hilsideDataClean/2019_csv'
clean_data_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_May_csv'

# def file_name_csv(raw_data_dir, clean_data_dir):
    # raw_data_dir : original data directory
    # clean_data_dir : targeted saved clean data directory

os.chdir(raw_data_dir)  # path of original csv data files
name = os.path.splitext(raw_data_dir)[0]  # get file name
raw_data_dir = os.getcwd()  # read current file path
#
file_list = []  # file name stored in file_list
for root, dirs, files in os.walk(raw_data_dir):
    for file in files:
        if os.path.splitext(file)[1] == '.csv':
            file_list.append(file)

# output the needed columns value under CleanESS directory with the same filename
new_path = clean_data_dir
# pd.read_csv
for path in file_list:
    data = pd.read_csv(path)
    df = pd.DataFrame(data, columns=["timestamp",
                                     "charge_discharge_power"
                                     ])
    df = df[0:2850]  # slice the first 2850 data points (23hr45min)
    print(len(df))
    if len(df) < 2850:
        continue

    # export to csv files
    df.to_csv(os.path.join(new_path, path), index=False)
"""

"""
# def house_time_csv(inputfile_dir, outputfile_dir, outputfile_name):
inputfile_dir = r'/Users/Huang/Documents/DQNBattery/data/house214_2019_May'
# inputfile_dir = r'/Users/Huang/Documents/hilsideDataClean/2019_csv_house214_May'
outputfile_dir = r'/Users/Huang/Documents/DQNBattery/data'
outputfile_name = r'testall.csv'
# csv_list = glob.glob(inputfile_dir)

os.chdir(inputfile_dir)
file_list = os.listdir()
file_list.sort()  # sort all data (from 01/01 to 12/31)
print(file_list)

df = pd.read_csv(inputfile_dir + '/' + file_list[0])
print(df)
df.to_csv(outputfile_dir + '/' + outputfile_name, index=False)

for i in range(1, len(file_list)):
    df = pd.read_csv(inputfile_dir + '/' + file_list[i], error_bad_lines=False)
    df.to_csv(outputfile_dir + '/' + outputfile_name, index=False, header=False, mode='a+')
"""

start = time.perf_counter()
a = r'/Users/Huang/Documents/DQNBattery/data/2019_weather_2station'
# a = '/Users/Huang/Documents/hilsideData/2019_csv'
os.chdir(a)  # change current dir to target csv data dir
a = os.getcwd()  # get current file dir

file_list = os.listdir(a)
file_list.sort()  # sort all data (from 01/01 to 12/31)

# file_list = []  # file name stored in file_list
# for root, dirs, files in os.walk(a):
#     for file in files:
#         if os.path.splitext(file)[1] == '.csv':
#             file_list.append(file)

# file_list = []  # file name stored in file_list
# for root, dirs, files in os.walk(a):
#     for file in files:
#         dirname, filename = os.path.split(file)
#         file_list.append(file)

csv_list = []
data_list = []
for csv in file_list:
    data = pd.read_csv(csv)
    # df = pd.DataFrame(data)
    data_list.append(len(data))
    csv_list.append(os.path.splitext(csv)[0])
    # print("date:", csv, "length: ", len(data))

# b = pd.DataFrame(csv_list, len(data_list))
# print(type(data_list))
b = {'dates': csv_list, 'length': data_list}
c = pd.DataFrame(b, columns=['dates', 'length'])

end = time.perf_counter()
# print("final is in ", end-start)
print("final took %s seconds" % (end-start))
