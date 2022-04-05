# MyData-Shield
MyData-Shield의 Batch type 입니다. <br/>
마이데이터 분석을 위하여 마아데이터에 포함한 개인정보 데이터를 가명/익명처리하는 프로젝트입니다.

### 테스트 환경
* Jupyter notebook
### 실행 환경
* python 3.6 이상
* pandas 1.4.1
* SQLAlcemy 1.4.32
* psycopg2-binary 2.9.3
* numpy 1.21.5
* pustil 5.9.0
### 금용 마이데이터 표준 API에 포함한 개인정보데이터 '항목명' 가명처리
* 개인정보로 생각되는 '항목명' 식별 및 설정
* 해당 데이터 형식에 맞게 정규 표현식 및 문자열 치환으로 마스킹처리
* 형식이 일정하여 예측가능한 개인정보데이터에 대한 가명처리
### 정규 표현식을 통한 가명처리 기능 구현
* 주민등록번호
* 이메일
* 전화번호
* 추가 예정
### 익명 처리한 데이터 DB연동 테스트
* PostgreSQL 기반의 ExperDB
* 대량의 데이터 처리시 메모리에 대한 문제 해결을 위해 일정량의 데이터 처리 후 DB에 추가하는 형식으로 구현

### 구성도
![image](https://user-images.githubusercontent.com/61214962/161666884-7ef86f4a-00ad-4b89-9a69-fd1b81f4477d.png)
