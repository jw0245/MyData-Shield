from mydata import Anonymyzation as anony

##### Costume area
### DB information that contains data requiring anonymization
host_r = ''
dbname_r = ''
username_r = ''
password_r = ''
port_r =''
table = ''
schema_r = ''

# resdata column : If there is no resdata, the object is deleted from 'table_target' after commenting out
column_r = ''

# Information needed for merging with additional pseudonymized columns
primary_key = ''

### DB information where data will be stored after anonymization
host_p = ''
dbname_p =''
username_p = ''
password_p = ''
port_p =''
schema_p = ''

# Table to contain anonymous/pseudonymized item names
target_table = ''

### Number of data to be processed at one time (variable = count)
data_c = 10000

### Waiting for data to be added next
time_c = 300

# Enter the name of the item requiring pseudonymization and the processing method.
table_target = {    
                
                'prn_no' : anony.faker.num_faker,
                'insu_seq' : anony.faker.num_faker,
                'x_api_tran_id' : anony.faker.x_api_tran_id,
                'api_tran_id' : anony.faker.api_tran_id,
                'insu_num' : anony.faker.insu_num,
                'account_num' : anony.faker.account_num,
                'client_id' : anony.faker.client_id,
                'client_secret' : anony.faker.client_secret,
                'domain' : anony.faker.domain,
                'ci' : anony.faker.ci,
                'corp_regno' : anony.faker.corp_regno,
                'regno' : anony.faker.regno,
                'domain_ip' : anony.faker.domain_ip,
                column_r : anony.faker.resdata,
                'ip' : anony.faker.ip,
                'redirect_uri' : anony.faker.redirect_uri
            }

### resdata pseudonymization items 
res_target = {

                'x_api_tran_id' : anony.faker.x_api_tran_id,
                'client_id' : anony.faker.client_id,
                'client_secret' : anony.faker.client_secret,
                'account_num' : anony.faker.account_num,
                'pp_id' : anony.Masking.p_data,
                'trans_id' : anony.Masking.p_num,
                'bond_num' : anony.Masking.p_num,
                'trans_memo' : anony.Masking.p_name,
                'repay_account_num' : anony.faker.account_num,
                'card_num' : anony.Masking.p_num,
                'account_name' : anony.faker.name_faker,
                'account_id' : anony.Masking.p_name,
                'charge_account_num' : anony.faker.account_num,
                'address' : anony.Masking.address,
                'car_number' : anony.Masking.p_car_num,
                'holder_name' : anony.faker.name_faker,
                'name' : anony.faker.name_faker,
                'pay_id' : anony.Masking.p_num,
                'trans_id' : anony.faker.num_faker,
                'insured_name' : anony.faker.name_faker,
                'user_ci' : anony.faker.num_faker,
                'ig_cs_no' : anony.faker.num_faker,
                'coverage_num' : anony.faker.coverage_num,
                'tx_id' : anony.faker.tx_id,
                'insu_num' : anony.faker.insu_num,
                'inuserd_no' : anony.faker.num_faker,
                'tx_id' : anony.faker.tx_id,
                'domain_ip' : anony.faker.domain_ip,
                'telecom_num' : anony.Masking.p_phone
              }
               

