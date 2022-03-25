
from mydata import Anonymyzation as anony

### DB information that contains data requiring anonymization
host_r = '182.252.133.38'
dbname_r = 'apim_sandbox'
user_r = 'apim_sandbox'
password_r = 'apim_sandbox'
port_r ='5433'
table_r = 'tb_test_data'
# mydata column
column_r = 'res_data'
# order in the table column to sort
seq_no = 'seq_no'

# not implemented
schema_r = ''

### DB information where data will be stored after anonymization
host_p = 'localhost'
dbname_p ='mydata'
user_p = 'experdba'
password_p = 'experdba'
port_p ='5432'
schema_p = 'myd'

# processing first data
table = 'mysd'

# append to an existing table
old_table = ''

# Table to contain anonymous/pseudonymized item names
target_table = 'target_table'

#When a new item name is added, the data in the previously processed table is added and saved after pseudonymization/anonymization
need_merge_table = 'need_merge_target'

### Number of data to be processed at one time (variable = n)
n = 1000
# The amount of data to be stored in the DB by dividing the processed data (variable = chunks)
chunks = 1000

# Registration and correction of data requiring pseudonymization
# anony.pseudonymy.[]
# p_data : unformatted data (ex : tasud1230asd- -> tasud12******)
# p_num : Account number, card number, and other numeric types 
# p_name : person's name (ex : (Lastname)**)
# p_car_name : Vehicle number format processing (ex : last 4 digits * )
# p_phone : Mobile number and customer number processing (ex: 010-0000-0000 -> 010-0000-****)
# adrress : Cut address data up to 2 words(only korean) (ex : OOO OOO OOO OOO -> OOO OOO)  

target_data = {
                'client_id' : anony.pseudonymy.p_data,
                'client_secret' : anony.pseudonymy.p_data,
                'account_num' : anony.pseudonymy.p_num,
                'pp_id' : anony.pseudonymy.p_data,
                'trans_id' : anony.pseudonymy.p_num,
                'bond_num' : anony.pseudonymy.p_num,
                'trans_memo' : anony.pseudonymy.p_name,
                'repay_account_num' : anony.pseudonymy.p_num,
                'card_num' : anony.pseudonymy.p_num,
                'account_name' : anony.pseudonymy.p_name,
                'account_id' : anony.pseudonymy.p_name,
                'charge_account_num' : anony.pseudonymy.p_num,
                'address' : anony.pseudonymy.address,
                'car_number' : anony.pseudonymy.p_car_name,
                'holder_name' : anony.pseudonymy.p_name,
                'name' : anony.pseudonymy.p_name,
                'pay_id' : anony.pseudonymy.p_num,
                'trans_id' : anony.pseudonymy.p_num,
                'insured_name' : anony.pseudonymy.p_name,
                'telecom_num' : anony.pseudonymy.p_num
              }