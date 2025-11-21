당신은 20년차 프로그램 코딩 전문가 입니다
다음과 같은 문제을 분석하여 결과치을 내되 반듯이 프롬프트 (JSON형식)로  풀고,검증 하세요
[문제]
📌 문제 4 — UPDATE 연습
✔ 요구사항
id = 2 인 학생의 나이를 25로 수정하시오.

📌 문제 5 — DELETE 연습
✔ 요구사항
id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.
📌 문제 6 — PRIMARY KEY 이해 문제
다음과 같은 테이블을 가정하시오:
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

아래 데이터 INSERT 시 발생할 문제를 설명하시오.
INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 B', 15000);

📌 질문:
어떤 에러가 발생하는가?

왜 발생하는가?

PRIMARY KEY 의 규칙을 쓰시오.

{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "문제 4",
      "title": "UPDATE 연습",
      "requirement": "id = 2 인 학생의 나이를 25로 수정하시오.",
      "database_context": "students 테이블 가정 (id, name, age 등의 컬럼 포함)",
      "solution_sql": "UPDATE students SET age = 25 WHERE id = 2;",
      "verification": {
        "description": "SQL 실행 후, SELECT * FROM students WHERE id = 2; 를 실행하여 age 컬럼 값이 25로 변경되었는지 확인합니다.",
        "test_case": [
          {"before": {"id": 2, "name": "Alice", "age": 20}},
          {"after": {"id": 2, "name": "Alice", "age": 25}}
        ]
      }
    },
    {
      "problem_id": "문제 5",
      "title": "DELETE 연습",
      "requirement": "id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.",
      "database_context": "students 테이블 가정 (id 컬럼 포함)",
      "solution_sql": "DELETE FROM students WHERE id = 3;",
      "verification": {
        "description": "SQL 실행 후, SELECT * FROM students WHERE id = 3; 를 실행하여 결과가 비어 있는지 (0 rows) 확인합니다.",
        "test_case": [
          {"before_count": "SELECT COUNT(*) FROM students; // N"},
          {"after_count": "SELECT COUNT(*) FROM students; // N-1"}
        ]
      }
    },
    {
      "problem_id": "문제 6",
      "title": "PRIMARY KEY 이해 문제",
      "requirement": "제공된 테이블 및 INSERT 문 분석 후 에러 발생 원인 및 PRIMARY KEY 규칙 설명.",
      "table_schema": "CREATE TABLE books (book_id INT PRIMARY KEY, title VARCHAR(100), price INT);",
      "insert_statements": [
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);",
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);"
      ],
      "analysis": {
        "error_type": "중복 키 에러 (Duplicate Key Error) 또는 무결성 제약 조건 위반 (Integrity Constraint Violation)",
        "error_explanation": "첫 번째 INSERT 문으로 `book_id`가 **1**인 레코드가 성공적으로 삽입되었습니다. 두 번째 INSERT 문은 `book_id`가 다시 **1**인 레코드를 삽입하려고 시도합니다. 그러나 `book_id` 컬럼은 **PRIMARY KEY**로 지정되어 있어, 테이블 내에서 **고유해야** 합니다. 따라서, 이미 존재하는 값인 '1'을 중복 삽입할 수 없어 에러가 발생합니다.",
        "primary_key_rules": [
          "**고유성 (Uniqueness):** PRIMARY KEY로 지정된 컬럼의 값은 테이블 내에서 **유일**해야 하며, 중복될 수 없습니다.",
          "**NOT NULL (비어있지 않음):** PRIMARY KEY로 지정된 컬럼은 **NULL 값**을 가질 수 없습니다. (테이블의 각 행을 식별할 수 있어야 하기 때문입니다.)",
          "**하나의 키:** 한 테이블에는 **오직 하나의 PRIMARY KEY**만 지정할 수 있습니다. (물론 여러 컬럼을 묶어 복합 PRIMARY KEY를 구성할 수는 있습니다.)"
        ]
      },
      "verification": {
        "description": "DBMS에 따라 'Duplicate entry '1' for key 'PRIMARY'' 또는 'ORA-00001: unique constraint (...) violated' 등의 에러 메시지가 출력될 것입니다."
      }
    }
  ]
}

{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "CREATE (INSERT) 기초",
      "title": "다중 레코드 삽입 연습",
      "requirement": "students 테이블에 id=1 (홍길동, 23), id=2 (이영희, 21), id=3 (박철수, 26) 데이터를 INSERT 하시오.",
      "database_context": "students 테이블 가정 (id, name, age 컬럼 포함)",
      "solution_sql": [
        "-- 1. 개별 INSERT 문 사용 (가장 기본적인 방법)",
        "INSERT INTO students (id, name, age) VALUES (1, '홍길동', 23);",
        "INSERT INTO students (id, name, age) VALUES (2, '이영희', 21);",
        "INSERT INTO students (id, name, age) VALUES (3, '박철수', 26);",
        "",
        "-- 2. 단일 INSERT 문으로 다중 레코드 삽입 (대부분의 SQL DBMS에서 권장)",
        "INSERT INTO students (id, name, age) VALUES",
        "(1, '홍길동', 23),",
        "(2, '이영희', 21),",
        "(3, '박철수', 26);"
      ],
      "verification": {
        "description": "SQL 실행 후, SELECT * FROM students; 를 실행하여 세 개의 새로운 레코드가 성공적으로 삽입되었는지 확인합니다.",
        "test_case": [
          {"id": 1, "name": "홍길동", "age": 23},
          {"id": 2, "name": "이영희", "age": 21},
          {"id": 3, "name": "박철수", "age": 26}
        ]
      }
    }
  ]
}

INSERT INTO students (id, name, age) VALUES (1, '홍길동', 23);

{
  "expert_profile": "20년차 프로그램 코딩 전문가",
  "problem_analysis_and_solution": [
    {
      "problem_id": "READ (SELECT) 기본 조회 - 1",
      "title": "전체 데이터 조회",
      "requirement": "students 테이블의 전체 데이터를 조회",
      "database_context": "students 테이블 가정",
      "solution_sql": "SELECT * FROM students;",
      "verification": {
        "description": "SQL 실행 시 students 테이블의 모든 행(레코드)과 모든 열(컬럼)이 반환되는지 확인합니다.",
        "expected_output_structure": ["id", "name", "age", "... (all columns)"]
      }
    },
    {
      "problem_id": "READ (SELECT) 기본 조회 - 2",
      "title": "조건부 조회 (숫자 비교)",
      "requirement": "나이가 22세 이상인 학생만 조회",
      "database_context": "students 테이블의 age 컬럼 사용",
      "solution_sql": "SELECT * FROM students WHERE age >= 22;",
      "verification": {
        "description": "반환된 결과 집합의 모든 레코드에서 age 컬럼 값이 22 또는 22보다 큰지 확인합니다.",
        "test_case_match": [
          {"age": 23, "match": "YES"},
          {"age": 22, "match": "YES"},
          {"age": 21, "match": "NO"}
        ]
      }
    },
    {
      "problem_id": "READ (SELECT) 기본 조회 - 3",
      "title": "조건부 조회 (문자열 일치)",
      "requirement": "name 이 “홍길동”인 학생만 조회",
      "database_context": "students 테이블의 name 컬럼 사용",
      "solution_sql": "SELECT * FROM students WHERE name = '홍길동';",
      "verification": {
        "description": "반환된 결과 집합의 모든 레코드에서 name 컬럼 값이 정확히 '홍길동'과 일치하는지 확인합니다. (DBMS에 따라 대소문자 구분을 확인해야 할 수도 있습니다.)",
        "test_case_match": [
          {"name": "홍길동", "match": "YES"},
          {"name": "홍길동1", "match": "NO"},
          {"name": "이영희", "match": "NO"}
        ]
      }
    }
  ]
}

