import mysql.connector

# mysql 연결 설정
connection = mysql.connector.connect(
    host = "localhost",      # mysql의 서버 주소를 입력하면 됨
    user = "root",           # 사용자 이름
    password = "1234",       # 비번임
    database = "python_test" # 사용할 데이터베이스를 입력
)

if connection.is_connected():
    print("MySQL에 성공적으로 연결되었습니다!")

connection.close()