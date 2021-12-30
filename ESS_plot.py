# plots of ess data
# modified data from raw data files
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as mticker
import numpy as np


data_dir = '/Users/Huang/Documents/OES_Log_Sample/CleanWeatherStation/WSHS_20190512.csv'
ess_dir = '/Users/Huang/Documents/OES_Log_Sample/ESS/F004_20190512.csv'
# ess_dir = '/Users/Huang/Documents/OES_Log_Sample/CleanESS/F004_20190512.cv'
# ess_dir = '/Users/Huang/Documents/hilsideDataClean/testall.csv'

data1 = pd.read_csv(data_dir)
data2 = pd.read_csv(ess_dir)

solar_rad = pd.DataFrame(data1, columns=["solar_radiation"])

# p1 = pd.to_numeric(data2['p1'], errors='coerce').fillna(method='ffill')
p1 = data2['p1'].fillna(method='ffill', inplace=False)
# print(p1[2369])
p2 = data2['p2'].fillna(method='ffill', inplace=False)
# p2 = pd.to_numeric(data2['p2'], errors='coerce').fillna(method='ffill')
# print(p2[2369])

# data for analyze
# rsoc discharge-charge
# rsoc = pd.to_numeric(data2['rsoc'], errors='coerce').fillna(method='ffill')
rsoc = data2['rsoc'].fillna(method='ffill', inplace=False)
rsoc_slice = rsoc[890:1600]  # slice from timestamp 890 to timestamp 1600

# chardischar = pd.to_numeric(data2['charge_discharge_power'], errors='coerce').fillna(method='ffill')
chardischar = data2['charge_discharge_power'].fillna(method='ffill', inplace=False)
chardischar_slice = chardischar[890:1600]


# consumption = np.add(data2['ups_output_power'], data2['p1'], -data2['p2'])
# print(consumption)
# print(data2.head())
data2.eval('consumption = ups_output_power + p1 - p2', inplace=True)
# print(data2)
print(data2['consumption'][2369])

plt.figure(1)
# plt.plot(rsoc, data2['consumption'])
line1, = plt.plot(data2['ups_output_power'], linestyle='-', label='ups_output')
line2, = plt.plot(data2['consumption'], linestyle='-', label='consumption')
line3, = plt.plot(data2['dcdc_battery_power'], linestyle='-', label='dcdc_battery')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)})
# plt.legend(handler_map={line2: HandlerLine2D(numpoints=4)})
# plt.grid()
plt.show()

# plt.figure(1)
# line1, = plt.plot(p1, linestyle='-', label='p1')
# line2, = plt.plot(p2, linestyle='-', label='p2')
# plt.title('p1 and p2 in 2019 for house 214')
# # p1" load curve for the house in one year
# # p2" PV curve for the house in one year
# plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
# plt.xlabel(r'time/h')
# plt.ylabel(r'$W$(AC)')
# plt.grid()
#
# plt.show()


'''
plt.figure(2)
plt.subplot(121)
plt.plot(solar_rad)
plt.title('solar radiation in a day')
plt.ylabel(r'$W/m^2$')
# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter(r'$W/m^2$'))
plt.grid()

plt.subplot(122)
line1, = plt.plot(p1, linestyle='-', label='p1')
line2, = plt.plot(p2, linestyle='-', label='p2')
plt.title('p1 and p2 in a day')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.ylabel(r'$W$(AC)')
plt.grid()

plt.show()
'''

# generate related variables
from numpy import mean
from numpy import std
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import seaborn as sns

