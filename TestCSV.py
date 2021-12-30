"""
import csv data files and output new csv files

Edit by Qiong
Date: June 2020
"""

# —*— coding: utf-8 —*—
import pandas as pd
import os
import re
import glob
import numpy as np
import random


def file_name_csv(raw_data_dir, clean_data_dir):
    # raw_data_dir : original data directory
    # clean_data_dir : targeted saved clean data directory

    os.chdir(raw_data_dir)  # path of original csv data files
    # name = os.path.splitext(raw_data_dir)[0]  # get file name
    raw_data_dir = os.getcwd()  # read current file path

    file_list = os.listdir(raw_data_dir)
    # file_list.sort()  # sort all data (from 01/01 to 12/31)

    # file_list = []  # file name stored in file_list
    # for root, dirs, files in os.walk(raw_data_dir):
    #     for file in files:
    #         if os.path.splitext(file)[1] == '.csv':
    #             file_list.append(file)

    # output the needed columns value under CleanESS directory with the same filename
    new_path = clean_data_dir
    for path in file_list:
        data = pd.read_csv(path)
        df = pd.DataFrame(data, columns=["timestamp",
                                         "charge_discharge_power",
                                         "rsoc",
                                         "battery_rsoc",
                                         "pvc_charge_power",
                                         "pvc_charge_current",
                                         "battery_current",
                                         "ups_output_power",
                                         "ups_output_current",
                                         "dcdc_grid_power",
                                         "p1",
                                         "p2"])
        # df = df[0:2850]  # slice the first 2850 data points (23hr45min)
        if len(df) < 2870:  # skip date if missing data points is too much
            continue

        if len(df) < 2880:  # extend missing data points to full 2880 points
            df = df.append(df.tail(2880 - len(df)), ignore_index=True)

        df = df[0:2880]

        # export to csv files
        df.to_csv(os.path.join(new_path, path), index=False)


def file_name_weather(raw_data_dir, clean_data_dir):
    # raw_data_dir : original data directory
    # clean_data_dir : targeted saved clean data directory

    os.chdir(raw_data_dir)  # path of original csv data files
    # name = os.path.splitext(raw_data_dir)[0]  # get file name
    raw_data_dir = os.getcwd()  # read current file path

    file_list = os.listdir(raw_data_dir)
    # file_list.sort()  # sort all data (from 01/01 to 12/31)

    # file_list = []  # file name stored in file_list
    # for root, dirs, files in os.walk(raw_data_dir):
    #     for file in files:
    #         if os.path.splitext(file)[1] == '.csv':
    #             file_list.append(file)

    # output the needed columns value under CleanESS directory with the same filename
    new_path = clean_data_dir
    for path in file_list:
        data = pd.read_csv(path)
        # df = pd.DataFrame(data, columns=["timestamp",
        #                                  "charge_discharge_power",
        #                                  "rsoc",
        #                                  "pvc_charge_power",
        #                                  "ups_output_power",
        #                                  "dcdc_grid_power",
        #                                  "p1",
        #                                  "p2"])
        df = pd.DataFrame(data, columns=["timestamp",
                                         "outside_temperature",
                                         "wind_speed",
                                         "solar_radiation"])

        # if len(df) < 2870:  # skip date if missing data points is too much
        #     continue
        #
        # if len(df) < 2880:  # extend missing data points to full 2880 points
        #     df = df.append(df.tail(2880 - len(df)), ignore_index=True)

        # export to csv files
        df.to_csv(os.path.join(new_path, path), index=False)


def weather_split(all_weather_data_dir, split_weather_dir):
    # all_weather_data_dir : all weather data directory
    # hillside_weather_dir : targeted house clean data directory

    os.chdir(all_weather_data_dir)  # path of original csv data files
    all_weather_data_dir = os.getcwd()  # read current file path

    file_list = []  # file name stored in file_list
    for root, dirs, files in os.walk(all_weather_data_dir):
        for file in files:
            dirname, filename = os.path.split(file)
            # filename.split('_', 1)[0]
            if filename.split('2019', 1)[0] == 'weather':
                #  'weather_' : hillside
                #  'weather' : 2 stations (hillside and tunnel entrance)
                file_list.append(file)

    # print(file_list)
    new_path = split_weather_dir
    for csv in file_list:
        data = pd.read_csv(csv)
        df = pd.DataFrame(data)
        # export to csv files
        df.to_csv(os.path.join(new_path, csv), index=False)


def hillside_csv(two_station_dir, hillside_dir):
    # for weather
    # two_station : two_station weather dir
    # hillside_dir : targeted saved hillside data directory

    os.chdir(two_station_dir)  # path of original csv data files
    # name = os.path.splitext(raw_data_dir)[0]  # get file name
    two_station_dir = os.getcwd()  # read current file path

    file_list = os.listdir(two_station_dir)
    file_list.sort()  # sort all data (from 01/01 to 12/31)

    # output the needed columns value under CleanESS directory with the same filename
    new_path = hillside_dir
    for path in file_list:
        data = pd.read_csv(path)
        df = pd.DataFrame(data, columns=["timestamp",
                                         "outside_temperature",
                                         "wind_speed",
                                         "solar_radiation"])
        df = df[2880:5760]  # slice the later 2880 data points (from hillside)

        # export to csv files
        df.to_csv(os.path.join(new_path, path), index=False)


def house_id_csv(allhouse_data_dir, onehouse_data_dir, houseID):
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


def house_time_csv(inputfile_dir, outputfile_dir, outputfile_name):
    # inputfile_dir = r'C:\Users\Administrator\PycharmProjects\house214Jan2019'
    # outputfile_dir = r'C:\Users\Administrator\PycharmProjects\house214Jan2019'
    # outputfile_name = r'testall.csv'
    # csv_list = glob.glob(inputfile_dir)

    os.chdir(inputfile_dir)
    file_list = os.listdir()
    file_list.sort()  # sort all data (from 01/01 to 12/31)

    df = pd.read_csv(inputfile_dir + '/' + file_list[0])

    df.to_csv(outputfile_dir + '/' + outputfile_name, index=False)

    for i in range(1, len(file_list)):
        df = pd.read_csv(inputfile_dir + '/' + file_list[i], error_bad_lines=False)
        df.to_csv(outputfile_dir + '/' + outputfile_name, index=False, header=False, mode='a+')


# allhouse_data_dir_2019 = '/Users/Huang/Documents/hilsideDataClean/2019_csv'
# onehouse_data_dir_2019 = '/Users/Huang/Documents/hilsideDataClean/2019_csv_house214'
# houseID = 'house214'
#
# house_id_csv(allhouse_data_dir_2019, onehouse_data_dir_2019, houseID)

# os.chdir('/Users/Huang/Documents/hilsideDataClean/2019_csv')
# file_chdir = os.getcwd()
#
# filecsv_list = []
# for root, dirs, files in os.walk(file_chdir):
#     for file in files:
#         dirname, filename = os.path.split(file)
#         # filename.split('_', 1)[0]
#         if filename.split('_', 1)[0] == 'house214':
#             print(file)
#             filecsv_list.append(file)
#
# # print(filecsv_list)
# path = r'/Users/Huang/Documents/hilsideDataClean/2019_csv_house214'
# for csv in filecsv_list:
#     data = pd.read_csv(csv)
#     df = pd.DataFrame(data)
#     # export to csv files
#     df.to_csv(os.path.join(path, csv), index=False)


def timeframe(timestep, inputdata):
    # select the timestamp with every timestep mins
    # slice data for every 15 minutes
    # raw data recorded for each 30s, ~ slice data for every timestep*2 rows
    step = np.arange(0, len(inputdata), timestep * 2)
    outputdata = inputdata.loc[step, :]
    outputdata.index = range(len(outputdata))  # do not keep original index
    return outputdata


def timeframe_avg(timestep, inputdata):
    inputdata = inputdata.fillna(method='ffill', inplace=False)
    avg = inputdata.groupby(inputdata.index // (timestep * 2)).mean()
    timestamp = timeframe(timestep, inputdata)
    time = timestamp[['timestamp']]
    outputdata = pd.concat((time, avg), axis=1)
    return outputdata


"""
# path of original csv data files
os.chdir('/Users/Huang/Documents/OES_Log_Sample/ESS/')
file_chdir = os.getcwd()

filecsv_list = []
for root, dirs, files in os.walk(file_chdir):
    for file in files:
        if os.path.splitext(file)[1] == '.csv':
            filecsv_list.append(file)

# output the needed columns value under CleanESS directory with the same filename
path = r'/Users/Huang/Documents/OES_Log_Sample/CleanESS/'
for csv in filecsv_list:
    data = pd.read_csv(csv)
    df = pd.DataFrame(data, columns=["timestamp", "charge_discharge_power", "rsoc", "pvc_charge_power", "ups_output_power",
                               "dcdc_grid_power", "p1", "p2"])
    # export to csv files
    df.to_csv(os.path.join(path, csv), index=False)
"""

# # create functions
# from sklearn.preprocessing import StandardScaler
# df_raw = pd.read_csv('/Users/Huang/Documents/DQNBattery/data/house214_2019_v1.csv')
# # df = df_raw.copy()
# df = df_raw.fillna(method='ffill', inplace=False)
# battery_rsoc = df.iloc[:, 2:3].values
# # sc_energy = StandardScaler(with_mean=False)
# # battery_rsoc = sc_energy.fit_transform(df.iloc[:, 2:3].values)  # rsoc
# rosc_max = np.max(battery_rsoc)
# rsoc_min = np.min(battery_rsoc)

# timestep = 2878  # one day
# ess_dir = '/Users/Huang/Documents/hilsideDataClean/house214_2019_all.csv'
# inputdata = pd.read_csv(ess_dir)
# # outputdata = timeframe(timestep, inputdata)
# # outputdata.to_csv('/Users/Huang/Documents/hilsideDataClean/house214_2019_v1.csv', index=False)
#
# # Total energy produced per month
# outputdata = inputdata.fillna(method='ffill', inplace=False)
# df2 = outputdata['pvc_charge_power']
#
# pv_year = []
# for i in range(365):
#     pv_day = np.max(df2[timestep * i: timestep * (i + 1) + 1])
#     pv_year.append(pv_day)
#
# print(pv_day)