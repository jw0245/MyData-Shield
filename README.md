# MyData-Shield
MyData-Shield의 Batch type 입니다. <br/>
마이데이터 분석을 위하여 마아데이터에 포함한 개인정보 데이터를 가명/익명처리하는 프로젝트입니다.

## 실행 환경
* OS : Window10 이상, Ubuntu 16 이상, Centos 7 이상
* PostgreSQL 
* python 3.6 이상

## 사용한 Python 외부 모듈
* pandas 1.3.5
* SQLAlchemy 1.4.36
* psycopg2-binary 2.9.3
* numpy 1.21.6
* psutil 5.9.0
* Faker 13.11.0

## 금용 마이데이터 표준 API에 포함한 개인정보데이터 '항목명' 가명처리
* 개인정보로 생각되는 '항목명' 식별 및 설정
* 해당 데이터 형식에 맞게 정규 표현식 및 문자열 치환으로 마스킹처리
* 형식이 일정하여 예측가능한 개인정보데이터에 대한 가명처리

## 가명 처리 기법
* Masking (ex : 123-124-1235 -> 123-*******-********)
* Faker (ex : 홍길동 -> 김철수)
* hash Encripytin (sha256)

## 익명 처리한 데이터 DB연동 테스트
* PostgreSQL에 저장
* 대량의 데이터 처리시 메모리에 대한 문제 해결을 위해 데이터를 일정 주기 및 수량으로 처리

## 구성도
![image](https://user-images.githubusercontent.com/61214962/161666884-7ef86f4a-00ad-4b89-9a69-fd1b81f4477d.png)

## 설정
1. **Config.py**의 DB정보 입력
  * **host_r, dbname_r, username_r, password_r, port_r, table, schema_r** 에 가명처리를 원하는 table이 존재하는 Postgrsql DB정보 입력
  * 해당 테이블에 **resdata**( JSON type )정보를 담은 칼럼을 **column_r**에 입력
  * **host_p, dbname_p, username_p, password_p, port_p, schema_p** 에 가명처리된 데이터가 저장될 Postgrsql DB정보 입력
  * 추가로 가명처리를 원하는 항목이 존재하면 **primary_key**에 입력
  * **target_table** 설정을 통해 resdata에 존재하는 가명 처리 항목명이 저장됨.

2. **Config.py** 가명처리 정보 입력
  * **data_c** (데이터를 한번 처리할 양), **time_c** (가명처리가 완료 후 추가 데이터가 생기는 확인 하는 '초' 단위 주기)
  * ```python
     table_target = { 
                      '항목명' = 가명 처리 방법,
                      column_r : anony.faker.resdata
                     }
     res_target = { 
                   '항목명' = 가명 처리 방법,
                   '항목명' = 가명 처리 방법
                  }
     
    ```
  -> table_target은 테이블안에 가명 처리를 원하는 칼럼명 및 처리 방법 입력, column_r은 테이블안에 resdata가 존재하면 사용, 존재하지 않으면 **주석처리** (가명 처리 방법은 3. 가명 처리 방법 설명 참고) 
  -> res_target = { '힝목명' = 가명 처리 방법 } resdata 내에 가명 처리를 원하는 항목명 및 처리 방법 입력
  
**3. 가명 처리 방법**

  ### Faker
  * anony.faker.fake_name  ( 홍길동 -> 최지현 )
  * anony.faker.fake_character  ( private_info - > OMeJZiramzaABneExVh)
  * anony.faker.fake_num  ( num_faker shows 10 random digits )
  * anony.faker.fake_id  ( secret_info -> kNTHhhYZkoKHahL5u7I2D)
  * anony.faker.account_num  ( 35600812438931 -> 3563368404692281)
  * anony.faker.client_id  ( 20-50 random character generation )
  * anony.faker.client_secret  ( random md5(), ex) 3asdk1j20asdkl1 -> 8451f734df34b7f66dd5fd820383f122
  * anony.faker.domain  ( 'naber.com' -> 'hangim.jusighoesa.baggimno.com')
  * anony.faker.fake_num8  ( num_faker shows 8 random digits )
  * anony.faker.fake_num13  ( num_faker shows 13 random digits )
  * anony.faker.fake_regno  ( 000-00-0000 -> 432-71-3211 )
  * anony.faker.fake_ip  ( 192.0.0.1 -> 104.67.80.197 )
  * anony.faker.redirect_uri  ( http://naber.com -> http://yuhanhoesa.kr/)
  * anony.faker.sha256  ( private_code -> 2d78ba29e9118929421ab2ab67db91208a770738aa0fad1b33e96cbbd092d042 )
  
  ### Masking
  * anoy.Masking.p_data  ( abcde1234 -> abcd***** )
  * anony.Masking.p_name  ( 홍길동 -> 홍** )
  * anony.Masking.p_car_num  ( 차량 09 1234 -> 차량 09 ****)
  * anony.Masking.p_phone  ( 01000000000 -> 0100000****)
  * anony.Masking.p_num  ( 350081243222278 -> 3500****4322****)
  * anony.Masking.address  ( 인천광역시 중구 봉은사14거리 -> 인천광역시 중구 )
  * aniny.Masking.hashText  ( satl + sha25(), ex) 홍길동 -> 831eec5830cb2b627d5829e9b61a8789d66e23c7b5a86f07e787a5ad77d4d0d1 )
  
## 실행

**Window**
* Python 가상환경 실행 ( env/Scipts )
```
> activate.bat
```
**Linux**
```
$ source activate
```

* MyDataShield 폴더에 위치한 main.py ( 실시간 가명처리 모듈 )
```
python main.py
```
* MyDataShield 폴더에 위치한 add_target.py ( 가명처리를 완료한 테이블이 존재하고 res_target에 가명 처리 항목이 추가 되었을때 사용 )
```
python add_target.py
```
  
   
