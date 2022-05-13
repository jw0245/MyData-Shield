# © 2022 LJW <gw0245@inzent.com>
import re
from faker import Faker
import random
import hashlib
import uuid

### target_data processing class(Masking, Faker)
### resdata processing function 

fake = Faker('ko-KR')

def anonymization(processed, target_data):
        # 추가로 식별 가능데이터가 있다면 아래 추가.   
        for key_r, value_r in processed.items():
            for key_p, value_p in target_data.items():
                if key_r == key_p:
                    print(value_p(value_r))
                    processed[key_r] = value_p(value_r)
                
### resdata(JSON 형태) 칼럼 내의 list 데이터들을 모두 찾고 anonymization 함수를 호출하여 가명처리
def Check_list(processed_list, target_data):

    ### 번으로 익명처리 함수를 돌려본다.
    ### 그 다음 value 값에 혹시 list가 있는지 확인 및 있으면 재귀 없으면 -> 함수 통과
    for index in range(len(processed_list)):
        #익명처리 함수
        anonymization(processed_list[index], target_data)
        for k in processed_list[index].keys():
            if 'list' in k:
                Check_list(processed_list[index][k], target_data)            
    return processed_list

### Create fake information by setting pseudonymized data as seed
class faker:
    
    def __init__():
        return ''

    # name form
    def fake_name(data):
        Faker.seed(data)
        trans_data = fake.name()
        print('fake_name : ' + trans_data)
        return trans_data
    
    # character_faker shows 19 corresponding random characters in seed
    def fake_character(data):
        Faker.seed(data)
        trans_data = fake.lexify('???????????????????')
        print(trans_data)
        return trans_data
    
    # num_faker shows 10 random digits
    def fake_num(data):
        Faker.seed(data)
        trans_data = fake.bothify(text='##########')
        print(trans_data)
        return trans_data
    
    # id(Fake data with 21 digits and letters)
    def fake_id(data):
        Faker.seed(data)
        trans_data = fake.lexify(text='?????????????????????', letters='ABCDEFGHIZKLMNOPQRSTUWYZabcdefghijklmnopqrstuwyz0123456789')
        print(trans_data)
        return trans_data
    
    # Data including resdata in json format
    def resdata(data, res_target) :

        # 기존에 있는 마스킹 기법으로 json 안에 존재하는 데이터 처리
        # string type 데이터 JSON으로 변환

        res_list = []
        try :
            
            if type(data) == str: 
                res_data = eval(data)
                res_list.append(res_data)
                Check_list(res_list, res_target)
                print('resdata',end=' ')
                print(' -> ',end=' ')
                print(str(res_list[0]))
                return str(res_list[0])
            
            else :
                res_data = data
                res_list.append(res_data)
                Check_list(res_list, res_target)
                print('resdata', end=' ')
                print(' -> ', end=' ')
                print(str(res_list[0]))
                return str(res_list[0])
            
        except SyntaxError as v:
            print('resdata is not in json format.')
            print(v)
            exit()
        
    # account_num
    def account_num(data) :
        Faker.seed(data)
        trans_data = fake.credit_card_number()
        print(trans_data)
        return trans_data
    
    # 20-50 random character generation
    def client_id(data) :
        Faker.seed(data)
        trans_data = fake.pystr( min_chars= 20 , max_chars = 50)
        print(trans_data)
        return trans_data
    
    # Generate encryption key corresponding to md5 type seed
    def client_secret(data) :
        Faker.seed(data)
        trans_data = fake.md5()
        print(trans_data)
        return trans_data
    
    # domain
    def domain(data) : 
        Faker.seed(data)
        random.seed(data)
        domain_dot = random.randint(1,5)
        trans_data = 'https://' + fake.domain_name(domain_dot)
        print(trans_data)
        return 'https://' + fake.domain_name(domain_dot)
    
    # ci 
    def fake_num8(data) : 
        Faker.seed(data)
        trans_data = fake.ean(length =8)
        print(trans_data)
        return trans_data
    
    # corp_regno
    def fake_num13(data) : 
        Faker.seed(data)
        trans_data = fake.ean(length = 13)
        print(trans_data)
        return trans_data
    
    # 000-00-0000 type regono
    def fake_regno(data) : 
        Faker.seed(data)
        trans_data = fake.bothify(text='###-##-####')
        print(trans_data)
        return trans_data
    

    def fake_ip(data):

        Faker.seed(data)
        trans_data = fake.ipv4_public()
        print(trans_data)
        return trans_data

    # redirect_uri
    def redirect_uri(data):

        Faker.seed(data)
        trans_data = fake.url()
        print(trans_data)
        return fake.url()

    # coverage_num
    def coverage_num(data):

        Faker.seed(data)
        trans_data = fake.bothify(text='##############')
        print(trans_data)
        return trans_data
    
    # sha256 암호화 코드 
    def sha256(data):

        Faker.seed(data)
        trans_data = fake.sha256()
        print(trans_data)
        return trans_data
  
    # pseudonymization of tx_id entries
    def tx_id(data) :

        tx_sp = data.split('_')
        tx_r = tx_sp[0] + '_' + tx_sp[1] + '_' + tx_sp[2] + '_' + tx_sp[3] + '_' + tx_sp[4] + '_' + '*' * len(tx_sp[-2]) + '_' + '*' * len(tx_sp[-1])  
        print(tx_r)
        return tx_r

# Maksing processing
class Masking :

    def __init__():

        return ''

    def p_data(data):
        
        # Data processing that is longer than 4 characters and has no special format(Half the length of the back is masked)
        if type(data) is not str:
            data = str(data)
            
        data_list = list(data)
        data_list[len(data) // 2 : ] = '*' * (len(data) - (len(data) // 2))
        return ''.join(data_list)
        
    # name pseudonymization function (All except last name are treated as *)
    def p_name(name) :
        
        if type(name) is not str:
            name = str(name)
            
        if len(name) >= 2:
            name_l = list(name)
            name_l[1:] = '*' * (len(name_l) -1) 
            return''.join(name_l)
        
        else :
            return ''
            
    # Vehicle number format processing(4 digits after masking)
    def p_car_num(car_num):
        
        if type(car_num) is not str:
            car_num = str(car_num)
        
        if len(car_num) >= 4:
            p_car = list(car_num)
            p_car[-4:] = '****'
            return ''.join(p_car)
        
        else :
            return ''

    # Mobile number and customer number processing(4 digits after masking)
    def p_phone(tel) :
        
        if type(tel) is not str:
            tel = str(tel)
            
        tel_re = re.compile(r'(\d{2,3})(\d{3,4})(\d{4})$')
        # Mobile number
        if tel_re.match(tel):
            return tel_re.sub('\g<1>\g<2>****',tel)

        # Customer information other than mobile phone number
        else :    
            num = list(tel)
            num[len(tel)//2:] = '*' * (len(tel) - len(tel)//2)
            return ''.join(num)

    # Pseudonymization of account numbers, card numbers and other payment methods                       
    def p_num(num):
        
        if type(num) is not str:
            num = str(num)
            
        account_re = re.compile(r'(\d{2,3})(\d{2,5})(\d{2,6})(\d{2,4})$')
        payment_re = re.compile(r'(\d{4})(\d{4})(\d{4})(\d{4})$')

        # card_num or account_num
        if payment_re.match(num):
            result = payment_re.sub('\g<1>****\g<3>****',num) 
            return result

        # account_num
        elif account_re.match(num):
            result = account_re.sub('\g<1>****\g<3>****',num) 
            return result

        # other payment methods
        else :
            a = list(num)
            a[len(a)//2 : ] = '*' * (len(num)-len(num) // 2)
            return ''.join(a)
        
    # Show Korean address up to 2 words      
    def address(ads) :
        ads_re = re.compile(r'([ㄱ-ㅣ가-힣]+[\s]+[ㄱ-ㅣ가-힣]+'')')
        if ads_re.match(ads) :
            return ads_re.findall(ads)[0]
        else :
            return ''

    # If you want salt+sha256 format encryption                   
    def hashText(text):
        
        if type(text) is not str:
            text = str(text)
            
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + text.encode()).hexdigest()
