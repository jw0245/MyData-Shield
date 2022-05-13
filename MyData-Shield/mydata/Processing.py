# © 2022 gw0245 <gw0245@inent.com>
import pandas as pd
from sqlalchemy import create_engine, Integer
import time
import psutil
from datetime import datetime
 
def inputdata(username_p, password_p, host_p, port_p, dbname_p, table, schema_p, data):

    db_info = "postgresql://" + username_p + ":" + password_p + "@" + host_p + ":" + port_p + "/" + dbname_p
    engine = create_engine(db_info)
    data.to_sql(name = table + '_faker',
                con = engine,
                schema = schema_p,
                if_exists = 'append',
                index = False )

def check_data(username_r, password_r, host_r, port_r, dbname_r, schema_r, table, username_p, password_p, host_p, port_p, dbname_p, schema_p, time_c):
    
    count = 0
    # Total number of rows in raw_table
    db_r = "postgresql://" + username_r + ":" + password_r + "@" + host_r + ":" + port_r + "/" + dbname_r
    engine_r = create_engine(db_r)
    count_r = pd.read_sql('SELECT count(*) FROM {schema}.{table_name}'.format(schema = schema_r, table_name = table), engine_r)

    # Whether a processing table exists
    db_p = "postgresql://" + username_r + ":" + password_r + "@" + host_r + ":" + port_r + "/" + dbname_r
    engine_p = create_engine(db_p)
    exists_table = pd.read_sql("select exists (select from information_schema.tables where table_schema = '{schema}' and table_name = '{table_name}')".format(schema = schema_r, table_name = table+'_faker'), engine_p)

    if exists_table['exists'][0]:
        count_p = pd.read_sql('SELECT count(*) FROM {schema}.{table_name}'.format(schema = schema_r, table_name = table+'_faker'), engine_p)
        
        if count_r['count'][0] - count_p['count'][0] > 0 :
            
            count = count_p['count'][0]
            print('Start at the ' + str(count) + 'total row')
            return count
        
        ### When the number of raw data and processed data is the same
        elif count_r['count'][0] - count_p['count'][0] == 0 :

            now = datetime.now()
            print("Time when there is no data to process : ", now.strftime('%Y-%m-%d %H:%M:%S'))
            print("Reprocess after " + str(time_c/60) + " minutes")

            time.sleep(time_c) #wait for time
            # 추가 데이터가 있는지 확인
            check_data(username_r, password_r, host_r, port_r, dbname_r, schema_r, table, username_p, password_p, host_p, port_p, dbname_p, schema_p)
            
    else :

        return count

def main(username_r, password_r, host_r, port_r, dbname_r, schema_r, table, table_target, column_r, res_target, username_p, password_p, host_p, port_p, dbname_p, schema_p, time_c, data_c) :
    
    now = datetime.now()
    print("Start time : ", now.strftime('%Y-%m-%d %H:%M:%S'))
    row = 0
    processing_time = 0
    while True :
        
        count = check_data(username_r, password_r, host_r, port_r, dbname_r, schema_r, table, username_p, password_p, host_p, port_p, dbname_p, schema_p, time_c)
        start = time.time()

        db_info = "postgresql://" + username_r + ":" + password_r + "@" + host_r + ":" + port_r + "/" + dbname_r
        engine = create_engine(db_info)
        data = pd.read_sql('SELECT * FROM {schema}.{table_name} OFFSET {count} limit {data_c}'.format(schema = schema_r, table_name = table, count = count, data_c = data_c), engine)
        now = datetime.now()

        print(str(len(data.index)) + ' row processing start time' + now.strftime('%Y-%m-%d %H:%M:%S') )
        for i in range(len(data.index)) : 
            for c, v in table_target.items() : 

                if c in data.columns and c == column_r : 

                    if (data[c][i] != 'N/A') and (data[c][i] != '') and (data[c][i] != None) and (data[c][i] != 'error') : 
                        data[c][i] =  v(data[c][i], res_target)

                elif c in data.columns:

                    if (data[c][i] != 'N/A') and (data[c][i] != '') and (data[c][i] != None) and (data[c][i] != 'error') : 
                        data[c][i] =  v(data[c][i])

        inputdata(username_p, password_p, host_p, port_p, dbname_p, table, schema_p, data)

        p = psutil.Process()
        rss = p.memory_info().rss / 2 ** 20 # Bytes to MB

        row += len(data.index)
        processing_time += time.time() - start

        print("number of rows processed " + str(row) + "row, processing time :", processing_time)               
        print(f"memory usage: {rss: 10.5f} MB")
        