# © 2022 LJW <gw0245@inzent.com>
import numpy as np # Version 1.21.5
import pandas as pd # Version  1.3.5
from sqlalchemy import create_engine, Integer
import psycopg2
from datetime import datetime

### Add pseudonymization table pseudonymization function 
def merge_table(conn_p, add_data, cur_p, table, column_r, primary_key, res_target, host_p, dbname_p, username_p, password_p, port_p, schema_p, table_target, data_c) :

    now = datetime.now()
    print("Start time of pseudonymization for new items : ", now.strftime('%Y-%m-%d %H:%M:%S'))

    db_info = "postgresql://" + username_p + ":" + password_p + "@" + host_p + ":" + port_p + "/" + dbname_p
    engine = create_engine(db_info)
    add_target = dict()

    # Mapping with additional item res_target vlaue contained in set
    for a in add_data :
        if a in res_target.keys():
            add_target[a] = res_target[a]

    cur_p.execute("SELECT COUNT(*) FROM {schema}.{table_name}".format(schema = schema_p, table_name = table+'_faker'))

    # Process 10,000 rows at a time
    len_data_row = cur_p.fetchall()[0][0]

    print('Total length of additional pseudonymized data : ' + str(len_data_row))

    for count in range(0, len_data_row, +10000):
       
        data = pd.read_sql('SELECT {pk}, {resdata} FROM {schema}.{table_name} OFFSET {count} limit {data_c}'.format(pk = primary_key, resdata = column_r, schema = schema_p, table_name = table+'_faker', count = count, data_c = data_c), engine)
        for i in range(len(data.index)) : 

            if (data[column_r][i] != 'N/A') and (data[column_r][i] != '') and (data[column_r][i] != None) and (data[column_r][i] != 'error') : 
                data[column_r][i] =  table_target[column_r](data[column_r][i], add_target)
       
        data.to_sql(name = table + '_update',
            con = engine,
            schema = schema_p,
            if_exists = 'append',
            index = False )

    #Update resdata
    cur_p.execute("UPDATE {schema}.{table_faker} set {resdata} = {schema}.{table_update}.{resdata} from {schema}.{table_update} where {schema}.{table_update}.{pk} = {schema}.{table_faker}.{pk}".format(schema = schema_p, table_faker = table+'_faker', table_update = table+'_update',resdata = column_r, pk = primary_key)) 
    conn_p.commit()
    print('Update completed on pseudonymization table')

    #drop temp table
    cur_p.execute("DROP TABLE {schema}.{table}".format(schema = schema_p, table = table+'_update'))
    conn_p.commit()
    print('Delete additional tables used for update')

    now = datetime.now()
    print("update completion end time : ", now.strftime('%Y-%m-%d %H:%M:%S'))

         
# Create table to store pseudonymized entries for resdata

def target_data_saved(res_target, table_target, host_p, dbname_p, username_p, password_p, schema_p, table, port_p, column_r, primary_key, data_c):
   
    if column_r == '' :
        return print('There is no resdata in this table.')

    conn_p = psycopg2.connect(host = host_p,
                              dbname = dbname_p,
                              user = username_p,
                              password = password_p,
                              port = int(port_p))

    cur_p = conn_p.cursor()
    cur_p.execute("CREATE TABLE IF NOT EXISTS {schema}.{target_table} (no Serial, target TEXT);".format(schema = schema_p, target_table = table+'_target'))
    conn_p.commit()
    
    cur_p.execute("select target from {schema}.{target_table};".format(schema = schema_p, target_table = table+'_target'))
    
    data = cur_p.fetchall()
    exists_columns = []

    # Previously processed data item name
    for v in data:
        exists_columns.append(v[0])

    # Comparison against resdata target
    add_data = set(res_target.keys()) - set(exists_columns)
    print('Added res_target list' + str(add_data))
    len_exists = len(exists_columns)

    # When additional pseudonymization items are created
    if add_data and len_exists > 0:

        print('Items that need to be merged')

        for add in add_data :
            cur_p.execute("insert into {schema}.{target_table} (target) values ('{target_data}')".format(schema = schema_p,
             target_table = table+'_target', target_data = str(add) ))
            conn_p.commit()
        merge_table(conn_p, add_data, cur_p, table, column_r, primary_key, res_target, host_p, dbname_p, username_p, password_p, port_p, schema_p, table_target, data_c)

    elif add_data : 
        
        print('Add item name to empty table_target')

        for add in add_data :
            cur_p.execute("insert into {schema}.{target_table} (target) values ('{target_data}')".format(schema = schema_p,
             target_table = table+'_target', target_data = str(add) ))
            conn_p.commit()
        
    conn_p.close()
