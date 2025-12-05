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

# cursor = connection.cursor()                   이러면 리스트 형태로 가져옴
cursor = connection.cursor(dictionary = True)   #이러면 딕셔너리 형태로 가져옴

cursor.execute("select * from users")  # users 테이블 내 모든 데이터 조회

rows = cursor.fetchall()
for row in rows:
    print(row)    # 각 행 출력

cursor.close()
connection.close()