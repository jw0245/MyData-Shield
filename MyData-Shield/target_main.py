import Config as cf
from sqlalchemy import create_engine, Integer
from mydata import add_target as tr
import os
import sys

### Used when there is an additional pseudonymization item for resdata

# Create log file for update process
log_count = 0
while os.path.exists("./log/" + cf.table + "_update_log" + str(log_count) + ".txt") :
    log_count += 1  
sys.stdout = open('./log/' + cf.table + '_update_log' + str(log_count) + '.txt', 'w')

try :

    tr.target_data_saved(cf.res_target, cf.table_target, cf.host_p, cf.dbname_p, cf.username_p, cf.password_p, cf.schema_p, cf.table, cf.port_p, cf.column_r, cf.primary_key, cf.data_c)

except Exception as e:
    print('#### ERORR #### : ', e)
    sys.stdout.close()