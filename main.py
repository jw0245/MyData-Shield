# MydataShield
import Config as cf
import numpy as np # Version 1.21.5
import pandas as pd # Version  1.3.5
import sqlalchemy # Version 1.4.31
from sqlalchemy import create_engine, Integer
from mydata import Processing as pr
from mydata import add_target as tr

### saved target item
tr.target_data_saved(cf.target_data, cf.host_p, cf.dbname_p, cf.user_p, cf.password_p, cf.schema_p, cf.target_table, cf.port_p, cf.old_table, cf.chunks, cf.need_merge_table)
pr.main(cf.host_r, cf.dbname_r, cf.user_r, cf.password_r, cf.table_r, cf.column_r, cf.seq_no, cf.port_r, cf.host_p, cf.dbname_p, cf.user_p, cf.password_p, cf.port_p, cf.table, cf.n, cf.chunks, cf.schema_r, cf.schema_p, cf.target_data)
