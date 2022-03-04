"""
Plots for power exchanges for houses
H214: it discharges a lot
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")


input_file_214 = '/Users/Huang/Documents/DQNBattery/data/house214_2019_sift_all.csv'
inputdata_214 = pd.read_csv(input_file_214)
df_214 = pd.DataFrame(inputdata_214, columns=["dcdc_grid_power"])

input_file_215 = '/Users/Huang/Documents/DQNBattery/data/house215_2019_sift_all.csv'
inputdata_215 = pd.read_csv(input_file_215)
df_215 = pd.DataFrame(inputdata_215, columns=["dcdc_grid_power"])

input_file_212 = '/Users/Huang/Documents/DQNBattery/data/house212_2019_sift_all.csv'
inputdata_212 = pd.read_csv(input_file_212)
df_212 = pd.DataFrame(inputdata_212, columns=["dcdc_grid_power"])

input_file_213 = '/Users/Huang/Documents/DQNBattery/data/house213_2019_sift_all.csv'
inputdata_213 = pd.read_csv(input_file_213)
df_213 = pd.DataFrame(inputdata_213, columns=["dcdc_grid_power"])

dcdc_power_214 = df_214.fillna(method='ffill', inplace=False)
# print(dcdc_power)
dcdc_power_215 = df_215.fillna(method='ffill', inplace=False)
dcdc_power_212 = df_212.fillna(method='ffill', inplace=False)
dcdc_power_213 = df_213.fillna(method='ffill', inplace=False)

fig, ax = plt.subplots(4, 1, sharey=True)

ax[0].plot(dcdc_power_214, 'g', label='exchanged power, H214')
ax[1].plot(dcdc_power_215, 'b', label='exchanged power, H215')
ax[2].plot(dcdc_power_212, 'k', label='exchanged power, H212')
ax[3].plot(dcdc_power_213, 'c', label='exchanged power, H213')
# plt.plot(dcdc_power_214, 'g', label='exchanged power')
# plt.plot(dcdc_power_215, 'g', label='exchanged power')
ax[0].legend(loc=2)
ax[1].legend(loc=2)
ax[2].legend(loc=2)
ax[3].legend(loc=2)

plt.show()

