import Config as cf
import re
import numpy as np # Version 1.21.5
import pandas as pd # Version  1.3.5
import sqlalchemy # Version 1.4.31
from sqlalchemy import create_engine, Integer
import psycopg2  #Version 2.9.3 
import time
from mydata import add_target as tr
import warnings

# Used when there is no added data and only a new item name is added
tr.target_data_saved(cf.target_data, cf.host_p, cf.dbname_p, cf.user_p, cf.password_p, cf.schema, cf.target_table, cf.port_p, cf.old_table, cf.chunks, cf.need_merge_table)
