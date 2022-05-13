# MyData-Shield
MyData-Shield의 Batch type 입니다. <br/>
마이데이터 분석을 위하여 마아데이터에 포함한 개인정보 데이터를 가명/익명처리하는 프로젝트입니다.

### 실행 환경
* OS : Window10 이상, Ubuntu 16 이상, Centos 7 이상
* PostgreSQL 
* python 3.6 이상

### Python 외부 모듈
* pandas 1.3.5
* SQLAlcemy 1.4.36
* psycopg2-binary 2.9.3
* numpy 1.21.6
* pustil 5.9.0
* faker 13.11.0

### 금용 마이데이터 표준 API에 포함한 개인정보데이터 '항목명' 가명처리
* 개인정보로 생각되는 '항목명' 식별 및 설정
* 해당 데이터 형식에 맞게 정규 표현식 및 문자열 치환으로 마스킹처리
* 형식이 일정하여 예측가능한 개인정보데이터에 대한 가명처리

### 가명 처리 기법
* Masking (ex : 123-124-1235 -> 123-***-****)
* Faker (ex : 홍길동 -> 김철수)
* hash Encripytin (sha256)
* 
* ### 익명 처리한 데이터 DB연동 테스트
* PostgreSQL에 저장
* 대량의 데이터 처리시 메모리에 대한 문제 해결을 위해 데이터를 일정 주기 및 수량으로 처리

### 구성도
![image](https://user-images.githubusercontent.com/61214962/161666884-7ef86f4a-00ad-4b89-9a69-fd1b81f4477d.png)

### 설정
1. **Config.py**의 DB정보 입력
  1) host_r, dbname_r, username_r, password_r, port_r, table, schema_r 에 가명처리를 원하는 table이 존재하는 Postgrsql DB정보 입력
  2) 해당 테이블에 resdata( log type )정보를 담은 칼럼을 column_r에 입력
  3) host_p, dbname_p, username_p, password_p, port_p, schema_p 에 가명처리된 데이터가 저장될 Postgrsql DB정보 입력
  4) 추가로 가명처리를 원하는 항목이 존재하면 primary_key에 입력
  5) target_table 설정을 통해 resdata에 존재하는 가명 처리 항목명이 저장됨.

2. **Config.py** 가명처리 정보 입력
  1) data_c(데이터를 한번 처리할 양), time_c(가명처리가 완료 후 추가 데이터가 생기는 확인 하는 '초' 단위 주기)
  2) table_target = { '항목명' = 가명 처리 방법, column_r : anony.faker.resdata } 테이블안에 가명 처리를 원하는 칼럼명 및 처리 방법 입력, column_r의 경우 테이블안에 resdata가   존재하면 사용, 존재하지 않으면 주석처리 
  3) res_target = { '힝목명' = 가명 처리 방법 }

