import psycopg2
import os

"""PostgreSQL 데이터베이스에 연결합니다."""


        # 환경 변수 또는 기본값으로 데이터베이스 연결 정보 설정
        db_host = "db_postgresql"
        db_port = "5432"
        db_name = "main_db"
        db_user = "admin"
        db_password = "admin123"
    conn = psycopg2.connect(
       host=db_host,
       port=db_port,
       dbname=db_name,
       user=db_user,
       password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")










