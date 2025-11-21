import psycopg2
import psycopg2.extras
import uuid

# --- 1. 데이터베이스 연결 설정 (참조 코드와 동일) ---
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = None
try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    print("✅ PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

    with conn.cursor() as cursor :
        print("-" * 40)
        
        # --- [문제 1] 테이블 생성 (PRIMARY KEY 기초) ---
        # PostgreSQL UUID 확장 설치
        cursor.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS students (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(50) NOT NULL,
            age INT
        );
        """
        cursor.execute(create_table_sql)
        print("✅ [문제 1] students 테이블 생성 완료 (UUID PRIMARY KEY).")

        # --- [문제 2] CREATE (INSERT) 기초 ---
        students_data = [
            ('홍길동', 23),
            ('이영희', 21),
            ('박철수', 26)
        ]
        # execute_values를 사용하여 다중 레코드 삽입
        psycopg2.extras.execute_values(
            cursor,
            "INSERT INTO students (name, age) VALUES %s",
            students_data
        )
        print(f"✅ [문제 2] 데이터 {cursor.rowcount}건 삽입 완료 (홍길동, 이영희, 박철수).")
        
        # 삽입된 데이터의 ID를 저장 (다음 UPDATE/DELETE에 사용)
        cursor.execute("SELECT id FROM students WHERE name = '이영희' LIMIT 1;")
        id_for_update = cursor.fetchone()[0] # id = 2 역할
        
        cursor.execute("SELECT id FROM students WHERE name = '박철수' LIMIT 1;")
        id_for_delete = cursor.fetchone()[0] # id = 3 역할

        
        # --- [문제 3] READ (SELECT) 기본 조회 ---
        print("\n--- [문제 3] READ (SELECT) 실행 ---")
        
        # 3-1. students 테이블의 전체 데이터를 조회
        cursor.execute("SELECT name, age FROM students;")
        print(f"   1. 전체 데이터 조회 ({cursor.rowcount}건): {cursor.fetchall()}")
        
        # 3-2. 나이가 22세 이상인 학생만 조회
        cursor.execute("SELECT name, age FROM students WHERE age >= 22;")
        print(f"   2. 나이 >= 22 조회 ({cursor.rowcount}건): {cursor.fetchall()}")
        
        # 3-3. name 이 “홍길동”인 학생만 조회
        cursor.execute("SELECT name, age FROM students WHERE name = %s;", ('홍길동',))
        print(f"   3. 이름이 '홍길동' 조회 ({cursor.rowcount}건): {cursor.fetchall()}")
        
        # --- [이전 문제] UPDATE 연습 ---
        print("\n--- UPDATE 실행 ---")
        update_sql = "UPDATE students SET age = 25 WHERE id = %s;"
        cursor.execute(update_sql, (id_for_update,))
        print(f"✅ [UPDATE] ID: {id_for_update} (이영희)의 나이를 25세로 수정 완료.")
        
        # 검증
        cursor.execute("SELECT age FROM students WHERE id = %s;", (id_for_update,))
        print(f"   > 수정 후 이영희 나이 확인: {cursor.fetchone()[0]}")

        # --- [이전 문제] DELETE 연습 ---
        print("\n--- DELETE 실행 ---")
        delete_sql = "DELETE FROM students WHERE id = %s;"
        cursor.execute(delete_sql, (id_for_delete,))
        print(f"✅ [DELETE] ID: {id_for_delete} (박철수) 데이터 삭제 완료.")
        
        # 검증
        cursor.execute("SELECT * FROM students WHERE id = %s;", (id_for_delete,))
        print(f"   > 삭제 후 박철수 데이터 존재 여부 (0이어야 함): {len(cursor.fetchall())}건")

        # --- [문제 6] PRIMARY KEY 이해 문제 (실제 에러 발생 테스트) ---
        print("\n--- PRIMARY KEY 에러 테스트 ---")
        try:
            # PostgreSQL은 '1'을 UUID로 자동 변환하려고 시도하며, 이는 일반적으로 실패함
            # 하지만, 에러 발생 시나리오 테스트를 위해 uuid 형식에 맞춰서 중복 값을 삽입 시도
            test_uuid = str(uuid.uuid4())
            
            # 1차 삽입 (성공)
            cursor.execute("INSERT INTO students (id, name, age) VALUES (%s, 'Test A', 99);", (test_uuid,))
            print("   1차 INSERT 성공.")

            # 2차 삽입 (PRIMARY KEY 제약 조건 위반 발생)
            cursor.execute("INSERT INTO students (id, name, age) VALUES (%s, 'Test B', 98);", (test_uuid,))
            
        except psycopg2.IntegrityError as e:
            print("❌ [문제 6] PRIMARY KEY 에러 발생 확인!")
            print(f"   > 에러 메시지: {e}")
            # 무결성 오류이므로 롤백 필요
            conn.rollback() 
        finally:
            print("✅ [문제 6] PRIMARY KEY의 중복 삽입 방지 기능 확인 완료.")

        # 최종 커밋 (롤백된 PRIMARY KEY 에러 제외 모든 작업 반영)
        conn.commit()

except psycopg2.Error as e:
    print(f"\n❌ 데이터베이스 연결 또는 작업 중 심각한 오류 발생: {e}")
finally:
    if conn:
        conn.close()
        print('\n--- PostgreSQL 연결이 종료되었습니다. ---')