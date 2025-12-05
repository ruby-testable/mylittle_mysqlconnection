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

cursor = connection.cursor() # 데이터베이스 작업을 위한 커서 객체 생성임

# 데이터 삽입 쿼리임
sql = "insert into users (name, email) values (%s, %s)" # 사용자 데이터를 추가하는 sql 쿼리
values = ("encore", "encore@example.com")               # 값으로 사용할 데이터

cursor.execute(sql, values) # 쿼리 실행
connection.commit()         # 변경 사항 커밋

print(f"{cursor.rowcount}개의 행이 추가되었습니다.") # 추가된 행 수 출력

cursor.close()
connection.close()

print("서버닫어잇")