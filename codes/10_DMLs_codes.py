{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "문제 1 & CREATE (INSERT) 기초 통합",
      "title": "students 테이블 생성 및 데이터 삽입",
      "requirement": [
        "students 테이블 생성: id (UUID PRIMARY KEY DEFAULT uuid_generate_v4()), name (VARCHAR(50)), age (INT)",
        "다음 데이터 INSERT: id=1(홍길동, 23), id=2(이영희, 21), id=3(박철수, 26) (단, ID는 UUID로 자동 생성되므로, ID 컬럼은 생략하고 name과 age만 삽입)"
      ],
      "database_context": "PostgreSQL 환경 및 psycopg2 라이브러리 사용",
      "solution_sql": [
        "-- 1. 테이블 생성 (PostgreSQL UUID 함수 사용)",
        "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";",
        "CREATE TABLE IF NOT EXISTS students (",
        "    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),",
        "    name VARCHAR(50) NOT NULL,",
        "    age INT",
        ");",
        "",
        "-- 2. 데이터 삽입 (ID는 자동으로 생성됨)",
        "INSERT INTO students (name, age) VALUES ('홍길동', 23), ('이영희', 21), ('박철수', 26);"
      ],
      "python_implementation": {
        "library": "psycopg2",
        "explanation": "참조 코드와 동일한 PostgreSQL 연결을 사용하여 CREATE TABLE 및 INSERT 작업을 수행합니다. UUID 생성을 위해 'uuid-ossp' 확장을 먼저 생성하는 코드를 포함합니다.",
        "code": [
          "import psycopg2",
          "",
          "# 데이터베이스 연결 정보 (참조 코드와 동일)",
          "db_host = \"db_postgresql\"",
          "db_port = \"5432\"",
          "db_name = \"main_db\"",
          "db_user = \"admin\"",
          "db_password = \"admin123\"",
          "",
          "try:",
          "    conn = psycopg2.connect(",
          "        host=db_host, port=db_port, dbname=db_name,",
          "        user=db_user, password=db_password",
          "    )",
          "    print(\"PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.\")",
          "",
          "    with conn.cursor() as cursor :",
          "        # 1. UUID 확장이 설치되어 있지 않은 경우를 대비하여 설치",
          "        cursor.execute(\"CREATE EXTENSION IF NOT EXISTS \\\"uuid-ossp\\\"\")",
          "",
          "        # 2. students 테이블 생성 (UUID PRIMARY KEY 사용)",
          "        create_table_sql = \"\"\"",
          "        CREATE TABLE IF NOT EXISTS students (",
          "            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),",
          "            name VARCHAR(50) NOT NULL,",
          "            age INT",
          "        );",
          "        \"\"\"",
          "        cursor.execute(create_table_sql)",
          "        print('students 테이블 생성 완료.')",
          "",
          "        # 3. 데이터 삽입 (다중 레코드 삽입)",
          "        insert_data_sql = \"\"\"",
          "        INSERT INTO students (name, age) VALUES ",
          "        ('홍길동', 23), ('이영희', 21), ('박철수', 26);",
          "        \"\"\"",
          "        cursor.execute(insert_data_sql)",
          "        print('데이터 3건 삽입 완료.')",
          "",
          "        # 4. 삽입된 데이터 확인 (검증)",
          "        cursor.execute(\"SELECT name, age, id FROM students WHERE name IN ('홍길동', '이영희', '박철수');\")",
          "        records = cursor.fetchall()",
          "        print('\\n--- 삽입된 레코드 확인 ---')",
          "        for name, age, uuid_id in records:",
          "            print(f'이름: {name}, 나이: {age}, ID: {uuid_id}')",
          "",
          "    conn.commit()",
          "except psycopg2.Error as e:",
          "    print(f\"데이터베이스 오류 발생: {e}\")",
          "finally:",
          "    if conn:",
          "        conn.close()",
          "        print('\\nPostgreSQL 연결이 종료되었습니다.')"
        ]
      },
      "verification": {
        "description": "Python 코드 실행 결과, 'students 테이블 생성 완료.' 메시지가 출력되고, 세 개의 레코드가 UUID와 함께 정상적으로 출력되는지 확인합니다.",
        "expected_output_pattern": [
          "이름: 홍길동, 나이: 23, ID: [UUID 값]",
          "이름: 이영희, 나이: 21, ID: [UUID 값]",
          "이름: 박철수, 나이: 26, ID: [UUID 값]"
        ]
      }
    }
  ]
}

{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "문제 2: CREATE (INSERT) 기초",
      "title": "students 테이블에 다중 데이터 삽입",
      "requirement": "students 테이블에 id=1 (홍길동, 23), id=2 (이영희, 21), id=3 (박철수, 26) 데이터를 INSERT 하시오. (UUID ID는 자동으로 생성된다고 가정)",
      "database_context": "PostgreSQL 환경 및 psycopg2 라이브러리 사용",
      "data_to_insert": [
        {"name": "홍길동", "age": 23},
        {"name": "이영희", "age": 21},
        {"name": "박철수", "age": 26}
      ],
      "solution_sql": [
        "-- 효율적인 단일 INSERT 문 (psycopg2.extras.execute_values 사용 시 내부적으로 생성되는 형태)",
        "INSERT INTO students (name, age) VALUES ('홍길동', 23), ('이영희', 21), ('박철수', 26);"
      ],
      "python_implementation": {
        "library": "psycopg2, psycopg2.extras",
        "explanation": "psycopg2.extras.execute_values를 사용하여 리스트 형태의 데이터를 단일 SQL 쿼리로 효율적으로 삽입합니다. 이 방식은 SQL 인젝션 공격을 방지하고 성능을 향상시킵니다.",
        "code": [
          "import psycopg2",
          "import psycopg2.extras",
          "",
          "# 데이터베이스 연결 정보 (참조 코드와 동일)",
          "db_host = \"db_postgresql\"",
          "db_port = \"5432\"",
          "db_name = \"main_db\"",
          "db_user = \"admin\"",
          "db_password = \"admin123\"",
          "",
          "conn = None",
          "try:",
          "    conn = psycopg2.connect(",
          "        host=db_host, port=db_port, dbname=db_name,",
          "        user=db_user, password=db_password",
          "    )",
          "    print(\"PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.\")",
          "",
          "    # 삽입할 데이터 (name, age)",
          "    students_data = [",
          "        ('홍길동', 23),",
          "        ('이영희', 21),",
          "        ('박철수', 26)",
          "    ]",
          "",
          "    with conn.cursor() as cursor :",
          "        # execute_values를 사용하여 다중 레코드 효율적으로 삽입",
          "        psycopg2.extras.execute_values(",
          "            cursor,",
          "            \"INSERT INTO students (name, age) VALUES %s\",",
          "            students_data",
          "        )",
          "        print(f'데이터 {cursor.rowcount}건 삽입 완료.')",
          "",
          "        # 삽입된 데이터 확인 (검증)",
          "        cursor.execute(\"SELECT name, age FROM students WHERE name IN ('홍길동', '이영희', '박철수');\")",
          "        records = cursor.fetchall()",
          "        print('\\n--- 삽입된 레코드 확인 ---')",
          "        for name, age in records:",
          "            print(f'이름: {name}, 나이: {age}')",
          "",
          "    conn.commit()",
          "except psycopg2.Error as e:",
          "    print(f\"데이터베이스 오류 발생: {e}\")",
          "finally:",
          "    if conn:",
          "        conn.close()",
          "        print('\\nPostgreSQL 연결이 종료되었습니다.')"
        ]
      },
      "verification": {
        "description": "Python 코드 실행 결과, '데이터 3건 삽입 완료.' 메시지가 출력되고, 세 개의 레코드(홍길동, 이영희, 박철수)가 정상적으로 출력되는지 확인합니다. ID는 자동으로 생성되어 확인 쿼리에서 제외했습니다.",
        "expected_output_pattern": [
          "이름: 홍길동, 나이: 23",
          "이름: 이영희, 나이: 21",
          "이름: 박철수, 나이: 26"
        ]
      }
    }
  ]
}


{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "문제 3: READ (SELECT) 기본 조회",
      "title": "다양한 조건에 따른 데이터 조회",
      "requirement": [
        "students 테이블의 전체 데이터 조회",
        "나이가 22세 이상인 학생만 조회",
        "name 이 '홍길동'인 학생만 조회"
      ],
      "database_context": "PostgreSQL 환경 및 psycopg2 라이브러리 사용",
      "solution_queries": {
        "query_1_all": "SELECT id, name, age FROM students;",
        "query_2_age_filter": "SELECT id, name, age FROM students WHERE age >= 22;",
        "query_3_name_filter": "SELECT id, name, age FROM students WHERE name = '홍길동';"
      },
      "python_implementation": {
        "library": "psycopg2",
        "explanation": "세 가지 다른 WHERE 절을 사용하여 students 테이블에서 데이터를 조회합니다. 각 쿼리 결과는 Python에서 fetchall()을 통해 가져옵니다.",
        "code": [
          "import psycopg2",
          "",
          "# 데이터베이스 연결 정보 (참조 코드와 동일)",
          "db_host = \"db_postgresql\"",
          "db_port = \"5432\"",
          "db_name = \"main_db\"",
          "db_user = \"admin\"",
          "db_password = \"admin123\"",
          "",
          "conn = None",
          "try:",
          "    conn = psycopg2.connect(",
          "        host=db_host, port=db_port, dbname=db_name,",
          "        user=db_user, password=db_password",
          "    )",
          "    print(\"PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.\")",
          "",
          "    with conn.cursor() as cursor :",
          "        # 1. students 테이블의 전체 데이터를 조회",
          "        print('\\n--- 1. 전체 데이터 조회 ---')",
          "        cursor.execute(\"SELECT id, name, age FROM students;\")",
          "        records_all = cursor.fetchall()",
          "        for record in records_all:",
          "            print(f'ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}')",
          "",
          "        # 2. 나이가 22세 이상인 학생만 조회",
          "        print('\\n--- 2. 나이 >= 22 필터링 ---')",
          "        cursor.execute(\"SELECT id, name, age FROM students WHERE age >= 22;\")",
          "        records_age = cursor.fetchall()",
          "        for record in records_age:",
          "            print(f'ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}')",
          "",
          "        # 3. name 이 '홍길동'인 학생만 조회",
          "        print('\\n--- 3. 이름 = '홍길동' 필터링 ---')",
          "        # Python에서는 SQL 문자열 내부에 따옴표를 사용할 때 이스케이프가 필요할 수 있습니다.",
          "        cursor.execute(\"SELECT id, name, age FROM students WHERE name = %s;\", ('홍길동',))",
          "        records_name = cursor.fetchall()",
          "        for record in records_name:",
          "            print(f'ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}')",
          "",
          "    # SELECT 쿼리는 데이터를 변경하지 않으므로 conn.commit()이 필수적이지 않습니다.",
          "except psycopg2.Error as e:",
          "    print(f\"데이터베이스 오류 발생: {e}\")",
          "finally:",
          "    if conn:",
          "        conn.close()",
          "        print('\\nPostgreSQL 연결이 종료되었습니다.')"
        ]
      },
      "verification": {
        "description": "Python 코드 실행 시, 각 쿼리의 결과가 요구 조건에 맞게 정확하게 필터링되어 출력되는지 확인합니다.",
        "key_concepts_used": [
          "SELECT * FROM [테이블] (전체 컬럼 조회)",
          "WHERE [컬럼] >= [값] (숫자 조건 필터링)",
          "WHERE [컬럼] = '[문자열]' (문자열 조건 필터링)",
          "psycopg2의 매개변수 바인딩 (%s)을 사용한 안전한 쿼리 실행"
        ]
      }
    }
  ]
}

{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "문제 6: PRIMARY KEY 이해 문제",
      "title": "UUID 기본 키를 사용한 중복 값 삽입 시 에러 분석",
      "table_schema": "CREATE TABLE books (book_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), title VARCHAR(100), price INT);",
      "insert_statements": [
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);",
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);"
      ],
      "analysis": {
        "error_type": "데이터 유형 불일치 오류 및 중복 키 에러 (Invalid Text Representation Error AND Duplicate Key Error)",
        "error_explanation": "이 시나리오에서는 두 가지 문제가 발생할 수 있습니다:",
        "issue_1_data_type": "books 테이블의 `book_id` 컬럼은 **UUID** 타입인데, INSERT 시 **숫자(1)**를 문자열(`'1'`) 없이 그대로 사용했습니다. PostgreSQL과 같은 엄격한 DBMS는 이를 유효한 UUID 문자열로 변환할 수 없어 **데이터 유형 불일치 오류**를 먼저 발생시킬 수 있습니다.",
        "issue_2_duplicate_key": "가정하고(또는 DBMS가 자동 형 변환을 수행하여) 첫 번째 INSERT가 성공적으로 **UUID 형태의 '1'**로 삽입되었다고 가정하면, 두 번째 INSERT 문은 동일한 키 값('1')을 다시 삽입하려고 시도합니다. `book_id`는 **PRIMARY KEY**이므로 **고유성(Uniqueness)** 규칙을 위반하여 **중복 키 에러**가 발생하고 삽입이 거부됩니다.",
        "final_error": "대부분의 경우, 첫 번째 단계인 **'중복 키 에러'**가 발생합니다. (UUID 타입이지만, 사용자가 명시적으로 동일한 값을 할당하려고 시도했기 때문에 고유성 제약 조건 위반이 주 원인입니다.)",
        "primary_key_rules": [
          "**1. 고유성 (Uniqueness):** 기본 키 값은 테이블 전체에서 **유일**해야 하며, 중복될 수 없습니다. (각 레코드를 명확하게 식별)",
          "**2. NOT NULL (비어있지 않음):** 기본 키 값은 **NULL**일 수 없습니다. (모든 레코드는 식별 값을 반드시 가져야 함)",
          "**3. 단일 키:** 하나의 테이블에는 **오직 하나의 PRIMARY KEY**만 지정 가능합니다. (복합 키는 가능)"
        ]
      },
      "verification": {
        "description": "DBMS는 두 번째 INSERT 문에서 PRIMARY KEY 제약 조건을 확인하고 'unique constraint violation' 등의 에러 메시지를 출력할 것입니다. "
      }
    }
  ]
}