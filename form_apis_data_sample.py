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
# sample_load
###################

demand = {}

cols = list(range(6, 52+1, 2))
cols.insert(0, 1)
# read column 2, col 7~53 for every 2 cols (1 hour per data point) from input data
# replace our own data files to the /Sample/ folder
demand_data = np.loadtxt('sample_load_data.csv', delimiter=',', skiprows=1, usecols=cols)

for row in demand_data:
    cus_id = "E{0:03d}".format(int(row[0]))
    if not demand.get(cus_id):
        demand[cus_id] = []
    demand[cus_id].append(row[1:])

for cus_id in demand:
    demand[cus_id] = np.array(demand[cus_id]) # change demand dict list(365) to ndarray (365, 24) for each house
    # gl.displayNames[cus_id]="Sample_"+cus_id
# """


###################
# sample_solar
###################

sol = np.loadtxt('sample_solar_data.csv', delimiter=',')
print(sol.size)

#######################
count_s = 0
# def old_pvcUpdate_Sample():
count_h=float(count_s)/3600
weight = count_h-int(count_h)
step_now=(int((count_h)/24)),int((count_h)%24)
step_next=(int((count_h+1)/24)),int((count_h+1)%24)
if int(count_h+1) >= sol.size:
    logger.debug("no more solar radiation data")
    # return False
# for oesid in gl.oesunits:
#     gl.oesunits[oesid]["emu"]["pvc_charge_power"]=round((1-weight)*sol[step_now]+ weight*sol[step_next],2) #sol[W]
#     # return True
