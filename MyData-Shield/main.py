# MydataShield
import Config as cf
import numpy as np # Version 1.21.5
import pandas as pd # Version  1.3.5
import sqlalchemy # Version 1.4.31
from sqlalchemy import create_engine, Integer
from mydata import add_target as tr
from mydata import Processing as pr
import os
import sys

# create log file
log_count = 0
while os.path.exists("./logs/" + cf.table + "_log" + str(log_count) + ".txt") :
    log_count += 1  
sys.stdout = open('./logs/' + cf.table + '_log' + str(log_count) + '.txt', 'w')

try :
    
    # main function execution
    tr.target_data_saved(cf.res_target, cf.table_target, cf.host_p, cf.dbname_p, cf.username_p, cf.password_p, cf.schema_p, cf.table, cf.port_p, cf.column_r, cf.primary_key, cf.data_c)
    pr.main(cf.username_r, cf.password_r, cf.host_r, cf.port_r, cf.dbname_r, cf.schema_r, cf.table, cf.table_target, cf.column_r, cf.res_target, cf.username_p, cf.password_p, cf.host_p, cf.port_p, cf.dbname_p, cf.schema_p, cf.time_c, cf.data_c)

except Exception as e:
    print('#### ERORR #### : ', e)
    sys.stdout.close()
    exit()

