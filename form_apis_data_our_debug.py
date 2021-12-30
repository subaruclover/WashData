# Data arrange for APIS use

import pandas as pd
import numpy as np
import logging.config, datetime
from copy import deepcopy
# import global_var as gl
# import config as conf
logger = logging.getLogger(__name__)


# """
###################
# house_load (h214)
###################

consumption = {}
col = list(range(2, 6, 1))
col.insert(0, 0)
our_data = np.loadtxt('house214_2019.csv', delimiter=',', skiprows=1, usecols=col)
# get the load column (2nd), house 214, 2019
# consumption = our_data[:, 1]
# print(int(len(our_data)/96))
day_len = int(len(our_data)/96)

for load_col in our_data:
    house_id = "E{0:03d}".format(int(load_col[0]))
    if not consumption.get(house_id):
        consumption[house_id] = []

for day in range(day_len):
    consumption[house_id].append(our_data[day*96:(day+1)*96, 1])


# 'E214' = {list:334} days of data
for house_id in consumption:
    consumption[house_id] = np.array(consumption[house_id])
    # gl.displayNames[cus_id]="Sample_"+cus_id

# load = consumption['E214']
# """

# """
###################
# house_pv (h214)
###################

col = list(range(2, 6, 1))
col.insert(0, 0)
# print(col)
our_data = np.loadtxt('house214_2019.csv', delimiter=',', skiprows=1, usecols=col)
# get the pvc_charge_power column (3rd), house 214, 2019
# pv = our_data[:, 2]
pv = {}

day_len = int(len(our_data)/96)

# for day in range(day_len):
#     pv.append(our_data[day*96:(day+1)*96, 2])

for load_col in our_data:
    house_id = "E{0:03d}".format(int(load_col[0]))
    if not pv.get(house_id):
        pv[house_id] = []

for day in range(day_len):
    pv[house_id].append(our_data[day*96:(day+1)*96, 2])


# 'E214' = {list:334} days of data
for house_id in pv:
    pv[house_id] = np.array(pv[house_id])

pv = pv[house_id]

# """

print(pv.size)
# count_s=0
#
# count_h = float(count_s) / 3600
# weight = count_h - int(count_h)
# step_now = int((count_h) / 24*4), int((count_h) % 24*4)
# step_next = (int((count_h + 1) / 24*4), int((count_h + 1) % 24*4))
# if int(count_h + 1) >= consumption['E214'].size:
#     logger.debug("no more consumption data")
#     return False
# for oesid in gl.oesunits:
#     gl.oesunits[oesid]["emu"]["ups_output_power"] = round(
#         ((1 - weight) * consumption[oesid][step_now] + weight * demand[oesid][step_next]), 2)  # consumption[W]

count_s = 0
# def old_pvcUpdate_Sample():
count_h=float(count_s)/3600
weight = count_h-int(count_h)
step_now=(int((count_h)/24*4)),int((count_h)%24*4)
step_next=(int((count_h+1)/24*4)),int((count_h+1)%24*4)

if int(count_h+1) >= pv.size:
    logger.debug("no more solar radiation data")

from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)
#
# run(host='localhost', port=8080)
powerflowToBattery = -300.3659
batteryVoltage = 48

if powerflowToBattery > 0:
    charge_discharge_power = round(powerflowToBattery, 2)
    battery_current = round(charge_discharge_power / batteryVoltage, 2)
    # logger.debug( i+ ": charge_disch "+ str(gl.oesunits[i]["emu"]["charge_discharge_power"]) + ", ACLoss: "+str(ACLoss) + ", DCLoss: " +str(DCLoss))
else:
    charge_discharge_power = - round(powerflowToBattery, 2)
    battery_current = -round(charge_discharge_power / batteryVoltage, 2)
    # logger.debug( i+ ": charge_disch "+ str(-gl.oesunits[i]["emu"]["charge_discharge_power"]) + ", ACLoss: "+str(ACLoss) + ", DCLoss: " +str(DCLoss))

