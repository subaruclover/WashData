#  plots
import pandas as pd
import os
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
from TestCSV import timeframe

from io import StringIO
from sklearn import linear_model, datasets
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
# sns.set()

data_dir = '/Users/Huang/Documents/OES_Log_Sample/CleanWeatherStation/WSHS_20190512.csv'
# ess_dir = '/Users/Huang/Documents/OES_Log_Sample/ESS/F004_20190512.csv'
# ess_dir = '/Users/Huang/Documents/OES_Log_Sample/CleanESS/F004_20190512.csv'

# ess_dir = '/Users/Huang/Documents/hilsideDataClean/house214_2019_May_v2.csv'
# ess_dir = '/Users/Huang/Documents/hilsideDataClean/2019_csv_house214/house214_20190512.csv'
ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_all.csv'
# ess_dir = '/Users/Huang/Documents/DQNBattery/data/house214_2019_quarterhour.csv'
# hillside_2019_quarterhour

data1 = pd.read_csv(data_dir)
data2 = pd.read_csv(ess_dir)

solar_rad = pd.DataFrame(data1, columns=["solar_radiation"])

# p1 = pd.to_numeric(data2['p1'], errors='coerce').fillna(method='ffill')
p1 = data2['p1'].fillna(method='ffill', inplace=False)
# print(p1[2369])
p2 = data2['p2'].fillna(method='ffill', inplace=False)
# p2 = pd.to_numeric(data2['p2'], errors='coerce').fillna(method='ffill')
# print(p2[2369])

rsoc = data2['rsoc'].fillna(method='ffill', inplace=False)
# rsoc_slice = rsoc[0:2878]
# 7 days [0:20150]
rsoc_slice = rsoc[0:20150]
# rsoc_slice = rsoc[0:669]  # 1st week of May
"""
battery current  
positive: input (charge), 
negative: output (discharge)
"""
battery_current = data2['battery_current'].fillna(method='ffill', inplace=False)
# battery_current_slice = battery_current[0:2878]
battery_current_slice = battery_current[0:20150]
# battery_current_slice = battery_current[0:669]
# print(battery_current[814])
# print(max(battery_current), min(battery_current))

# bat_cur_max = np.max(battery_current)
# bat_cur_min = np.min(battery_current)
# print(bat_cur_max, bat_cur_min)

Battery_Current = np.sign(battery_current)  # -1, 0, 1
# print(Battery_Current)

'''
# data for analyze
# rsoc discharge-charge
# rsoc = pd.to_numeric(data2['rsoc'], errors='coerce').fillna(method='ffill')
rsoc = data2['rsoc'].fillna(method='ffill', inplace=False)
rsoc_slice = rsoc[890:1600]  # slice from timestamp 890 to timestamp 1600

# chardischar = pd.to_numeric(data2['charge_discharge_power'], errors='coerce').fillna(method='ffill')
chardischar = data2['charge_discharge_power'].fillna(method='ffill', inplace=False)
chardischar_slice = chardischar[890:1600]
'''

DATA2 = timeframe(timestep=15, inputdata=data2)
RSOC = DATA2['rsoc'].fillna(method='ffill', inplace=False)
BATTERY_CURRENT = DATA2['battery_current'].fillna(method='ffill', inplace=False)
# print(RSOC, BATTERY_CURRENT)

"""
# plt.plot(rsoc, battery_current)
# plt.scatter(battery_current_slice.cumsum(), rsoc_slice)
plt.scatter(battery_current.cumsum(), rsoc, color='seagreen', label='train data', s=1)
# plt.scatter(BATTERY_CURRENT.cumsum(), RSOC)
plt.ylabel(r'rsoc (%)')
plt.xlabel(r'cumulated battery current (A(DC))')
"""

"""
# model
regr = linear_model.LinearRegression()
# fitting
regr.fit(battery_current_slice.cumsum().values.reshape(-1, 1), rsoc_slice)  # reshape(-1, 1)，as X is one-dim

# coef_ and intercept_
w0, w1 = regr.intercept_, regr.coef_
"""
# """
X_train = battery_current_slice.cumsum()
y_train = rsoc_slice
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_train, y_train, train_size=0.8, random_state=0)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
# build model and training
regr_model = linear_model.LinearRegression()
regr_model.fit(X_train, y_train)
print('Coefficients:%s, intercept %s' % (regr_model.coef_, regr_model.intercept_))
print('Score: %.2f' % regr_model.score(X_test, y_test))

w0, w1 = regr_model.intercept_, regr_model.coef_
w0 = float(w0)
w1 = float(w1)
print('The regression function of this model is y = {} + {} * x'.format(w0, w1))

# plot
plt.scatter(X_train, y_train, color='seagreen', label='train data', s=1)
plt.scatter(X_test, y_test, color='darkorange', label='test data', s=1)
plt.xlabel('cumulated battery current (A(DC))')
plt.ylabel('rsoc (%)')

# fitting curve
Y_train_pred = regr_model.predict(X_train)
plt.plot(X_train, Y_train_pred, color='black', label='best line')

plt.legend(loc=2)
plt.grid()
plt.show()
# """

# line1, = plt.plot(rsoc, linestyle='-', label='rsoc')
# line2, = plt.plot(battery_current, linestyle='-', label='battery_current')
# plt.title('battery char/dischar VS rsoc of May 2019 of house214')
# plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
# plt.xlabel(r'time/15min')
# plt.ylabel(r'A(DC) / %')
# my_y_ticks = np.arange(0, 110, 10)
# plt.yticks(my_y_ticks)

# plt.grid()
# plt.show()

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

"""
# generate related variables
from numpy import mean
from numpy import std
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import seaborn as sns


# calculate covariance matrix
covariance = cov(rsoc_slice, chardischar_slice)
# print(covariance)
# calculate Pearson's correlation
corr, _ = pearsonr(rsoc_slice, chardischar_slice)
# print('Pearsons correlation: %.3f' % corr)

# calculate spearman's correlation
corr, _ = spearmanr(rsoc_slice, chardischar_slice)
# print('Spearmans correlation: %.3f' % corr)
"""

# diff = rsoc.diff()
# plt.plot(diff)
# plt.show()

'''
plt .figure(3)
plt.subplot(2, 4, 1)
line1, = plt.plot(rsoc, linestyle='-', label='rsoc')
line2, = plt.plot(chardischar, linestyle='-', label='char')
plt.title('rsoc and charge_discharge_power on May 12th for F004')
# rsoc: Relative State Of Charge of battery for display
# chardischar: output/input power from/to BMU; always positive (?)
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.xlabel(r'time/30s')
plt.ylabel(r'$W$(DC)/%')
plt.grid()

plt.subplot(2, 4, 5)
line1, = plt.plot(rsoc_slice, linestyle='-', label='rsoc')
line2, = plt.plot(chardischar_slice, linestyle='-', label='char')
plt.title('slice from timestamp 890 to timestamp 1600')
# rsoc: Relative State Of Charge of battery for display
# chardischar: output/input power from/to BMU; always positive (?)
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.xlabel(r'time/30s')
plt.ylabel(r'$W$(DC)/%')
plt.grid()

plt.subplot(2, 4, 2)
plt.scatter(rsoc, chardischar)
plt.xlabel('rsoc/%')
plt.ylabel('charge_dischar_power/W')
plt.title('all day')

plt.subplot(2, 4, 6)
plt.scatter(rsoc_slice, chardischar_slice)
plt.xlabel('rsoc_slice/%')
plt.ylabel('charge_dischar_power/W')
# plt.title('slice from timestamp 890 to timestamp 1600')

# Integral of charge_discharge_power over time during the day VS. rsoc
plt.subplot(2, 4, 3)
plt.plot(rsoc, chardischar.cumsum())

plt.subplot(2, 4, 7)
plt.plot(rsoc_slice, chardischar_slice.cumsum())

plt.subplot(2, 4, 4)
plt.plot(chardischar, rsoc.diff())
# plt.plot(rsoc.diff())

plt.subplot(2, 4, 8)
plt.plot(chardischar_slice, rsoc_slice.diff())


plt.show()
'''

"""
df = pd.DataFrame(data2, columns=["charge_discharge_power",
                                  "rsoc"])
df = df.fillna(method='ffill', inplace=False)

# df = pd.to_numeric(data2["charge_discharge_power"], errors='coerce').fillna(method='ffill')
# print(df.iloc[2369, :])

# plt.figure(4)
# # plt.subplot(1, 2, 1)
# plt.matshow(df.corr())
# # plt.subplot(1, 2, 2)
# # sns.heatmap(df)
# plt.show()


# Integral of charge_discharge_power over time during the day
# DataFrame.cumsum() function
# changing trend of RSOC value during the day
# print(chardischar.cumsum())
# plt.plot(chardischar.cumsum())
# plt.show()

# slice data for every 15 minutes
# raw data recorded for each 30s, ~ slice data for every 30 rows
step = np.arange(0, len(data2), 30)
df2 = data2.loc[step, :]
df2.index = range(len(df2))  # do not keep original index
# print(df2)

# plt.plot(df2['p1'])
# plt.show()
line1, = plt.plot(df2['rsoc'], linestyle='-', label='rsoc')
line2, = plt.plot(df2['charge_discharge_power'], linestyle='-', label='char')
plt.title('rsoc and charge_discharge_power for house 214 in year 2019')
# rsoc: Relative State Of Charge of battery for display
# chardischar: output/input power from/to BMU; always positive (?)
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.xlabel(r'time/15min')
plt.ylabel(r'$W$(DC)/%')
plt.grid()
plt.show()
"""