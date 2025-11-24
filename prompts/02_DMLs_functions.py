{
  "요청_분석_및_문제_정의": "PostgreSQL 데이터베이스에 특정 스키마를 가진 'books' 테이블을 생성하는 Python 함수(create_books_table) 개발",
  "전문가_검토_사항": [
    "PostgreSQL 연결을 위해 psycopg2 라이브러리 사용 가정",
    "UUID 기본값 설정을 위한 'uuid-ossp' 확장 활성화 단계 포함",
    "테이블 스키마의 무결성 및 자료형 일치 여부 확인"
  ],
  "요구사항_검증_항목": {
    "함수명": "create_books_table()",
    "데이터베이스_종류": "PostgreSQL",
    "테이블명": "books",
    "컬럼_스키마": [
      {"컬럼명": "id", "자료형": "UUID", "제약조건": "PRIMARY KEY", "기본값": "uuid_generate_v4()"},
      {"컬럼명": "title", "자료형": "VARCHAR(100)"},
      {"컬럼명": "price", "자료형": "INT"}
    ]
  }
}

import psycopg2
from psycopg2 import sql
import sys

# PostgreSQL 연결 정보 (실제 환경에 맞게 수정 필요)
# 주의: 이 라이브러리를 사용하려면 'pip install psycopg2-binary'를 실행해야 합니다.
DB_CONFIG = {
    'host': 'localhost',
    'database': 'your_database_name', # 실제 데이터베이스 이름으로 변경하세요
    'user': 'your_user_name',         # 실제 사용자 이름으로 변경하세요
    'password': 'your_password'       # 실제 비밀번호로 변경하세요
}

def create_books_table():
    """
    PostgreSQL 데이터베이스에 연결하여 'books' 테이블을 생성합니다.
    UUID 생성을 위해 'uuid-ossp' 확장이 활성화됩니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 'uuid-ossp' 확장 활성화 (UUID 기본값 사용을 위해 필수)
        print("PostgreSQL 확장을 확인하고 활성화합니다...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

        # 3. 테이블 생성 SQL
        # IF NOT EXISTS를 사용하여 테이블이 이미 존재하는 경우 오류를 방지합니다.
        table_creation_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100) NOT NULL,
                price INT
            );
        """)

        # 4. SQL 실행
        cur.execute(table_creation_query)
        
        # 5. 변경 사항 커밋 및 커서 종료
        conn.commit()
        cur.close()
        
        # 6. 요구사항에 맞는 출력
        print("books 테이블이 생성되었습니다.")

    except psycopg2.Error as e:
        # 데이터베이스 연결 및 쿼리 실행 중 발생한 오류 처리
        print(f"데이터베이스 오류가 발생했습니다: {e}", file=sys.stderr)
        # 롤백: 오류 발생 시 커밋되지 않은 모든 변경 사항을 취소
        if conn:
            conn.rollback()
    except Exception as e:
        # 기타 예외 처리
        print(f"일반 오류가 발생했습니다: {e}", file=sys.stderr)
    finally:
        # 연결 종료 (오류가 발생하더라도 반드시 실행되어야 함)
        if conn:
            conn.close()
            print("데이터베이스 연결이 종료되었습니다.")

if __name__ == '__main__':
    # 메인 실행 가이드: 함수를 호출하여 테이블 생성 프로세스를 시작합니다.
    print("--- [문제 1] books 테이블 생성 프로세스 시작 ---")
    create_books_table()
    print("--- 프로세스 완료 ---")

    import psycopg2
from psycopg2 import sql
import sys

# PostgreSQL 연결 정보 (실제 환경에 맞게 수정 필요)
# 주의: 이 라이브러리를 사용하려면 'pip install psycopg2-binary'를 실행해야 합니다.
DB_CONFIG = {
    'host': 'localhost',
    'database': 'your_database_name', # 실제 데이터베이스 이름으로 변경하세요
    'user': 'your_user_name',         # 실제 사용자 이름으로 변경하세요
    'password': 'your_password'       # 실제 비밀번호로 변경하세요
}

def create_books_table():
    """
    PostgreSQL 데이터베이스에 연결하여 'books' 테이블을 생성합니다.
    UUID 생성을 위해 'uuid-ossp' 확장이 활성화됩니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 'uuid-ossp' 확장 활성화 (UUID 기본값 사용을 위해 필수)
        print("PostgreSQL 확장을 확인하고 활성화합니다...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

        # 3. 테이블 생성 SQL
        # IF NOT EXISTS를 사용하여 테이블이 이미 존재하는 경우 오류를 방지합니다.
        table_creation_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100) NOT NULL,
                price INT
            );
        """)

        # 4. SQL 실행
        cur.execute(table_creation_query)
        
        # 5. 변경 사항 커밋 및 커서 종료
        conn.commit()
        cur.close()
        
        # 6. 요구사항에 맞는 출력
        print("books 테이블이 성공적으로 생성되었습니다.")

    except psycopg2.Error as e:
        # 데이터베이스 연결 및 쿼리 실행 중 발생한 오류 처리
        print(f"데이터베이스 오류 (테이블 생성): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        # 기타 예외 처리
        print(f"일반 오류 (테이블 생성): {e}", file=sys.stderr)
    finally:
        # 연결 종료 (오류가 발생하더라도 반드시 실행되어야 함)
        if conn:
            conn.close()
            print("테이블 생성 후 데이터베이스 연결이 종료되었습니다.")


def insert_books():
    """
    'books' 테이블에 테스트 도서 데이터를 삽입합니다.
    UUID는 자동 생성되므로 쿼리에서 제외합니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 테스트 데이터 (title, price 순서)
        # ID는 DEFAULT 설정에 의해 자동으로 채워지므로 데이터에 포함하지 않습니다.
        books_data = [
            ("파이썬 입문", 19000),
            ("알고리즘 기초", 25000),
            ("네트워크 이해", 30000),
        ]
        
        # 3. 데이터 삽입 SQL
        # title과 price만 명시하고, 값에 %s 플레이스홀더 사용
        insert_query = sql.SQL("INSERT INTO books (title, price) VALUES (%s, %s);")
        
        # 4. 다중 SQL 실행 (executemany)
        print("도서 데이터를 삽입합니다...")
        cur.executemany(insert_query, books_data)
        
        # 삽입된 행의 수 확인
        inserted_count = cur.rowcount 
        
        # 5. 변경 사항 커밋 및 커서 종료
        conn.commit()
        cur.close()
        
        # 6. 요구사항에 맞는 출력
        print(f"{inserted_count}개 도서가 삽입되었습니다.")

    except psycopg2.Error as e:
        # 데이터베이스 연결 및 쿼리 실행 중 발생한 오류 처리
        print(f"데이터베이스 오류 (데이터 삽입): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        # 기타 예외 처리
        print(f"일반 오류 (데이터 삽입): {e}", file=sys.stderr)
    finally:
        # 연결 종료
        if conn:
            conn.close()
            print("데이터 삽입 후 데이터베이스 연결이 종료되었습니다.")


if __name__ == '__main__':
    # 메인 실행 가이드: 테이블 생성 후 데이터 삽입 함수를 순차적으로 호출합니다.
    print("--- [문제 1] books 테이블 생성 및 데이터 삽입 프로세스 시작 ---")
    
    # 1. 테이블 생성
    create_books_table()

    # 2. 데이터 삽입
    # (테이블이 성공적으로 생성되었다고 가정하고 진행)
    insert_books()
    
    print("--- 프로세스 완료 ---")

    import psycopg2
from psycopg2 import sql
import sys

# PostgreSQL 연결 정보 (실제 환경에 맞게 수정 필요)
# 주의: 이 라이브러리를 사용하려면 'pip install psycopg2-binary'를 실행해야 합니다.
DB_CONFIG = {
    'host': 'localhost',
    'database': 'your_database_name', # 실제 데이터베이스 이름으로 변경하세요
    'user': 'your_user_name',         # 실제 사용자 이름으로 변경하세요
    'password': 'your_password'       # 실제 비밀번호로 변경하세요
}

# --- 테이블 생성 함수 ---

def create_books_table():
    """
    PostgreSQL 데이터베이스에 연결하여 'books' 테이블을 생성합니다.
    UUID 생성을 위해 'uuid-ossp' 확장이 활성화됩니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 'uuid-ossp' 확장 활성화 (UUID 기본값 사용을 위해 필수)
        print("PostgreSQL 확장을 확인하고 활성화합니다...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

        # 3. 테이블 생성 SQL
        table_creation_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100) NOT NULL,
                price INT
            );
        """)

        # 4. SQL 실행
        cur.execute(table_creation_query)
        
        # 5. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        print("books 테이블이 성공적으로 생성되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (테이블 생성): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (테이블 생성): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("테이블 생성 후 데이터베이스 연결이 종료되었습니다.")

# --- 데이터 삽입 함수 ---

def insert_books():
    """
    'books' 테이블에 테스트 도서 데이터를 삽입합니다.
    UUID는 자동 생성되므로 쿼리에서 제외합니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 테스트 데이터 (title, price 순서)
        books_data = [
            ("파이썬 입문", 19000),
            ("알고리즘 기초", 25000),
            ("네트워크 이해", 30000),
        ]
        
        # 3. 데이터 삽입 SQL
        insert_query = sql.SQL("INSERT INTO books (title, price) VALUES (%s, %s);")
        
        # 4. 다중 SQL 실행 (executemany)
        print("도서 데이터를 삽입합니다...")
        cur.executemany(insert_query, books_data)
        
        # 삽입된 행의 수 확인
        inserted_count = cur.rowcount 
        
        # 5. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        print(f"{inserted_count}개 도서가 삽입되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (데이터 삽입): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (데이터 삽입): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("데이터 삽입 후 데이터베이스 연결이 종료되었습니다.")


# --- 데이터 조회 함수들 ---

def get_all_books():
    """
    'books' 테이블의 모든 도서 데이터를 조회합니다.
    """
    conn = None
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 모든 데이터 조회
        cur.execute("SELECT id, title, price FROM books;")
        books = cur.fetchall()
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (전체 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (전체 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
    
    return books

def get_expensive_books():
    """
    가격이 25000원 이상인 도서 데이터를 조회합니다.
    """
    conn = None
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 가격 조건으로 조회
        cur.execute("SELECT id, title, price FROM books WHERE price >= 25000;")
        books = cur.fetchall()
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (고가 도서 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (고가 도서 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            
    return books

def get_book_by_title(title: str):
    """
    제목(title)이 일치하는 도서 데이터를 조회합니다.
    파라미터화된 쿼리를 사용합니다.
    """
    conn = None
    book = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # title 조건으로 조회 (파라미터 사용)
        select_query = "SELECT id, title, price FROM books WHERE title = %s;"
        cur.execute(select_query, (title,)) # title을 튜플 형태로 전달
        book = cur.fetchone() # 하나의 결과만 가져옴
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (제목으로 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (제목으로 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            
    return book


# --- 메인 실행 블록 ---

def print_books(title, books_list):
    """조회 결과를 깔끔하게 출력하는 헬퍼 함수"""
    print(f"\n--- {title} 결과 ---")
    if books_list:
        # 컬럼 헤더 출력 (간소화)
        print(f"{'ID':<38} | {'Title':<15} | {'Price':<8}")
        print("-" * 65)
        for book in books_list:
            # UUID는 길기 때문에 앞 8자리만 표시
            book_id_short = str(book[0])[:8] + "..."
            title_val = book[1]
            price_val = book[2]
            print(f"{book_id_short:<38} | {title_val:<15} | {price_val:<8,}")
    else:
        print("조회된 도서 데이터가 없습니다.")
    print("-" * 65)


if __name__ == '__main__':
    # 메인 실행 가이드: 테이블 생성 -> 데이터 삽입 -> 데이터 조회 순으로 실행합니다.
    print("=====================================================")
    print("--- [문제 1] books 테이블 CRUD 프로세스 시작 ---")
    print("=====================================================")
    
    # 1. 테이블 생성 및 'uuid-ossp' 확장 활성화
    create_books_table()

    # 2. 테스트 데이터 삽입
    insert_books()

    # 3. 데이터 조회 테스트
    print("\n[데이터 조회 기능 테스트 시작]")
    
    # 3-1. 전체 조회 함수 테스트
    all_books = get_all_books()
    print_books("전체 조회 (get_all_books)", all_books)

    # 3-2. 가격이 25000원 이상인 데이터 조회 함수 테스트
    expensive_books = get_expensive_books()
    print_books("가격 25000원 이상 조회 (get_expensive_books)", expensive_books)

    # 3-3. title 이 “파이썬 입문”인 데이터 조회 함수 테스트
    target_title = "파이썬 입문"
    book_by_title = get_book_by_title(target_title)
    
    # get_book_by_title은 단일 행을 반환하므로 리스트 형태로 변환하여 출력 함수에 전달
    result_list = [book_by_title] if book_by_title else []
    print_books(f"제목 '{target_title}' 조회 (get_book_by_title)", result_list)
    
    print("=====================================================")
    print("--- 모든 프로세스 완료 ---")
    print("=====================================================")

    import psycopg2
from psycopg2 import sql
import sys

# PostgreSQL 연결 정보 (실제 환경에 맞게 수정 필요)
# 주의: 이 라이브러리를 사용하려면 'pip install psycopg2-binary'를 실행해야 합니다.
DB_CONFIG = {
    'host': 'localhost',
    'database': 'your_database_name', # 실제 데이터베이스 이름으로 변경하세요
    'user': 'your_user_name',         # 실제 사용자 이름으로 변경하세요
    'password': 'your_password'       # 실제 비밀번호로 변경하세요
}

# --- 테이블 생성 함수 ---

def create_books_table():
    """
    PostgreSQL 데이터베이스에 연결하여 'books' 테이블을 생성합니다.
    UUID 생성을 위해 'uuid-ossp' 확장이 활성화됩니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 'uuid-ossp' 확장 활성화 (UUID 기본값 사용을 위해 필수)
        print("PostgreSQL 확장을 확인하고 활성화합니다...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

        # 3. 테이블 생성 SQL
        table_creation_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100) NOT NULL,
                price INT
            );
        """)

        # 4. SQL 실행
        cur.execute(table_creation_query)
        
        # 5. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        print("books 테이블이 성공적으로 생성되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (테이블 생성): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (테이블 생성): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("테이블 생성 후 데이터베이스 연결이 종료되었습니다.")

# --- 데이터 삽입 함수 ---

def insert_books():
    """
    'books' 테이블에 테스트 도서 데이터를 삽입합니다.
    UUID는 자동 생성되므로 쿼리에서 제외합니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 테스트 데이터 (title, price 순서)
        books_data = [
            ("파이썬 입문", 19000),
            ("알고리즘 기초", 25000),
            ("네트워크 이해", 30000),
        ]
        
        # 3. 데이터 삽입 SQL
        insert_query = sql.SQL("INSERT INTO books (title, price) VALUES (%s, %s);")
        
        # 4. 다중 SQL 실행 (executemany)
        print("도서 데이터를 삽입합니다...")
        cur.executemany(insert_query, books_data)
        
        # 삽입된 행의 수 확인
        inserted_count = cur.rowcount 
        
        # 5. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        print(f"{inserted_count}개 도서가 삽입되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (데이터 삽입): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (데이터 삽입): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("데이터 삽입 후 데이터베이스 연결이 종료되었습니다.")


# --- 데이터 조회 함수들 ---
# (이전과 동일)

def get_all_books():
    """
    'books' 테이블의 모든 도서 데이터를 조회합니다.
    """
    conn = None
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 모든 데이터 조회
        cur.execute("SELECT id, title, price FROM books;")
        books = cur.fetchall()
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (전체 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (전체 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
    
    return books

def get_expensive_books():
    """
    가격이 25000원 이상인 도서 데이터를 조회합니다.
    """
    conn = None
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 가격 조건으로 조회
        cur.execute("SELECT id, title, price FROM books WHERE price >= 25000;")
        books = cur.fetchall()
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (고가 도서 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (고가 도서 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            
    return books

def get_book_by_title(title: str):
    """
    제목(title)이 일치하는 도서 데이터를 조회합니다.
    파라미터화된 쿼리를 사용합니다.
    """
    conn = None
    book = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # title 조건으로 조회 (파라미터 사용)
        select_query = "SELECT id, title, price FROM books WHERE title = %s;"
        cur.execute(select_query, (title,)) # title을 튜플 형태로 전달
        book = cur.fetchone() # 하나의 결과만 가져옴
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (제목으로 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (제목으로 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            
    return book

# --- 데이터 업데이트 함수 ---

def update_second_book_price():
    """
    저장된 순서(title ASC 기준)에서 두 번째 도서의 가격을 27000원으로 변경합니다.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 1. '저장된 순서' (title ASC)에서 두 번째 도서의 UUID를 조회합니다.
        # OFFSET 1은 두 번째 레코드를 의미합니다.
        select_uuid_query = """
            SELECT id FROM books
            ORDER BY title ASC
            LIMIT 1 OFFSET 1;
        """
        cur.execute(select_uuid_query)
        result = cur.fetchone()

        if result is None:
            print("업데이트할 두 번째 도서를 찾지 못했습니다.")
            return

        book_id_to_update = result[0]
        new_price = 27000

        # 2. 조회된 UUID를 사용하여 가격을 업데이트합니다.
        update_query = "UPDATE books SET price = %s WHERE id = %s;"
        cur.execute(update_query, (new_price, book_id_to_update))
        
        updated_count = cur.rowcount

        # 3. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        if updated_count > 0:
            print(f"두 번째 도서 (ID: {str(book_id_to_update)[:8]}...) 가격이 {new_price:,}원으로 수정되었습니다.")
        else:
            print("업데이트된 도서가 없습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (업데이트): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (업데이트): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("데이터 업데이트 후 데이터베이스 연결이 종료되었습니다.")


# --- 메인 실행 블록 ---

def print_books(title, books_list):
    """조회 결과를 깔끔하게 출력하는 헬퍼 함수"""
    print(f"\n--- {title} 결과 ---")
    if books_list:
        # 컬럼 헤더 출력 (간소화)
        print(f"{'ID':<38} | {'Title':<15} | {'Price':<8}")
        print("-" * 65)
        for book in books_list:
            # UUID는 길기 때문에 앞 8자리만 표시
            book_id_short = str(book[0])[:8] + "..."
            title_val = book[1]
            price_val = book[2]
            print(f"{book_id_short:<38} | {title_val:<15} | {price_val:<8,}")
    else:
        print("조회된 도서 데이터가 없습니다.")
    print("-" * 65)


if __name__ == '__main__':
    # 메인 실행 가이드: 테이블 생성 -> 데이터 삽입 -> 업데이트 -> 변경 확인 순으로 실행합니다.
    print("=====================================================")
    print("--- [문제 1] books 테이블 CRUD 프로세스 시작 ---")
    print("=====================================================")
    
    # 1. 테이블 생성 및 'uuid-ossp' 확장 활성화
    create_books_table()

    # 2. 테스트 데이터 삽입
    insert_books()

    # 3. 업데이트 전 상태 확인
    print("\n[업데이트 전 전체 도서 목록 확인]")
    all_books_before_update = get_all_books()
    print_books("업데이트 전 전체 도서", all_books_before_update)
    
    # 4. 데이터 업데이트 실행
    print("\n[데이터 업데이트 실행]")
    update_second_book_price()

    # 5. 업데이트 후 상태 확인
    print("\n[업데이트 후 전체 도서 목록 확인]")
    all_books_after_update = get_all_books()
    print_books("업데이트 후 전체 도서", all_books_after_update)

    # 6. 이전 조회 함수들 테스트 (선택적 재실행)
    print("\n[데이터 조회 기능 재 테스트]")
    
    target_title = "파이썬 입문"
    book_by_title = get_book_by_title(target_title)
    result_list = [book_by_title] if book_by_title else []
    print_books(f"제목 '{target_title}' 조회 (get_book_by_title)", result_list)

    expensive_books = get_expensive_books()
    print_books("가격 25000원 이상 조회 (get_expensive_books)", expensive_books)

    print("=====================================================")
    print("--- 모든 프로세스 완료 ---")
    print("=====================================================")

    import psycopg2
from psycopg2 import sql
import sys

# PostgreSQL 연결 정보 (실제 환경에 맞게 수정 필요)
# 주의: 이 라이브러리를 사용하려면 'pip install psycopg2-binary'를 실행해야 합니다.
DB_CONFIG = {
    'host': 'localhost',
    'database': 'your_database_name', # 실제 데이터베이스 이름으로 변경하세요
    'user': 'your_user_name',         # 실제 사용자 이름으로 변경하세요
    'password': 'your_password'       # 실제 비밀번호로 변경하세요
}

# --- 테이블 생성 함수 ---

def create_books_table():
    """
    PostgreSQL 데이터베이스에 연결하여 'books' 테이블을 생성합니다.
    UUID 생성을 위해 'uuid-ossp' 확장이 활성화됩니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 'uuid-ossp' 확장 활성화 (UUID 기본값 사용을 위해 필수)
        print("PostgreSQL 확장을 확인하고 활성화합니다...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

        # 3. 테이블 생성 SQL
        table_creation_query = sql.SQL("""
            DROP TABLE IF EXISTS books CASCADE; -- 이전 테스트를 위해 테이블 초기화
            CREATE TABLE books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100) NOT NULL,
                price INT
            );
        """)

        # 4. SQL 실행
        cur.execute(table_creation_query)
        
        # 5. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        print("books 테이블이 성공적으로 생성되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (테이블 생성): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (테이블 생성): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("테이블 생성 후 데이터베이스 연결이 종료되었습니다.")

# --- 데이터 삽입 함수 ---

def insert_books():
    """
    'books' 테이블에 테스트 도서 데이터를 삽입합니다.
    UUID는 자동 생성되므로 쿼리에서 제외합니다.
    """
    conn = None
    try:
        # 1. PostgreSQL 데이터베이스 연결
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 2. 테스트 데이터 (title, price 순서)
        books_data = [
            ("파이썬 입문", 19000),
            ("알고리즘 기초", 25000),
            ("네트워크 이해", 30000),
        ]
        
        # 3. 데이터 삽입 SQL
        insert_query = sql.SQL("INSERT INTO books (title, price) VALUES (%s, %s);")
        
        # 4. 다중 SQL 실행 (executemany)
        print("도서 데이터를 삽입합니다...")
        cur.executemany(insert_query, books_data)
        
        # 삽입된 행의 수 확인
        inserted_count = cur.rowcount 
        
        # 5. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        print(f"{inserted_count}개 도서가 삽입되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (데이터 삽입): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (데이터 삽입): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("데이터 삽입 후 데이터베이스 연결이 종료되었습니다.")


# --- 데이터 조회 함수들 ---

def get_all_books():
    """
    'books' 테이블의 모든 도서 데이터를 조회합니다.
    """
    conn = None
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 모든 데이터 조회
        cur.execute("SELECT id, title, price FROM books;")
        books = cur.fetchall()
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (전체 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (전체 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
    
    return books

def get_expensive_books():
    """
    가격이 25000원 이상인 도서 데이터를 조회합니다.
    """
    conn = None
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 가격 조건으로 조회
        cur.execute("SELECT id, title, price FROM books WHERE price >= 25000;")
        books = cur.fetchall()
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (고가 도서 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (고가 도서 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            
    return books

def get_book_by_title(title: str):
    """
    제목(title)이 일치하는 도서 데이터를 조회합니다.
    파라미터화된 쿼리를 사용합니다.
    """
    conn = None
    book = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # title 조건으로 조회 (파라미터 사용)
        select_query = "SELECT id, title, price FROM books WHERE title = %s;"
        cur.execute(select_query, (title,)) # title을 튜플 형태로 전달
        book = cur.fetchone() # 하나의 결과만 가져옴
        
        cur.close()

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (제목으로 조회): {e}", file=sys.stderr)
    except Exception as e:
        print(f"일반 오류 (제목으로 조회): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            
    return book

# --- 데이터 업데이트 함수 ---

def update_second_book_price():
    """
    저장된 순서(title ASC 기준)에서 두 번째 도서의 가격을 27000원으로 변경합니다.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 1. '저장된 순서' (title ASC)에서 두 번째 도서의 UUID를 조회합니다. (OFFSET 1)
        select_uuid_query = """
            SELECT id FROM books
            ORDER BY title ASC
            LIMIT 1 OFFSET 1;
        """
        cur.execute(select_uuid_query)
        result = cur.fetchone()

        if result is None:
            print("업데이트할 두 번째 도서를 찾지 못했습니다.")
            return

        book_id_to_update = result[0]
        new_price = 27000

        # 2. 조회된 UUID를 사용하여 가격을 업데이트합니다.
        update_query = "UPDATE books SET price = %s WHERE id = %s;"
        cur.execute(update_query, (new_price, book_id_to_update))
        
        updated_count = cur.rowcount

        # 3. 변경 사항 커밋
        conn.commit()
        cur.close()
        
        if updated_count > 0:
            print(f"두 번째 도서 (ID: {str(book_id_to_update)[:8]}...) 가격이 {new_price:,}원으로 수정되었습니다.")
        else:
            print("업데이트된 도서가 없습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (업데이트): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (업데이트): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("데이터 업데이트 후 데이터베이스 연결이 종료되었습니다.")

# --- 데이터 삭제 함수 ---

def delete_third_book():
    """
    저장된 순서(title ASC 기준)에서 세 번째 도서 데이터를 삭제합니다.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 1. '저장된 순서' (title ASC)에서 세 번째 도서의 UUID를 조회합니다. (OFFSET 2)
        select_uuid_query = """
            SELECT id, title FROM books
            ORDER BY title ASC
            LIMIT 1 OFFSET 2;
        """
        cur.execute(select_uuid_query)
        result = cur.fetchone()

        if result is None:
            print("삭제할 세 번째 도서를 찾지 못했습니다.")
            return

        book_id_to_delete = result[0]
        book_title_deleted = result[1]

        # 2. 조회된 UUID를 사용하여 도서를 삭제합니다.
        delete_query = "DELETE FROM books WHERE id = %s;"
        cur.execute(delete_query, (book_id_to_delete,))

        deleted_count = cur.rowcount

        # 3. 변경 사항 커밋
        conn.commit()
        cur.close()

        if deleted_count > 0:
            print(f"세 번째 도서 ('{book_title_deleted}')가 삭제되었습니다.")
        else:
            print("삭제된 도서가 없습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류 (삭제): {e}", file=sys.stderr)
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"일반 오류 (삭제): {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("데이터 삭제 후 데이터베이스 연결이 종료되었습니다.")


# --- 메인 실행 블록 ---

def print_books(title, books_list):
    """조회 결과를 깔끔하게 출력하는 헬퍼 함수"""
    print(f"\n--- {title} 결과 ---")
    if books_list:
        # 컬럼 헤더 출력 (간소화)
        print(f"{'ID':<38} | {'Title':<15} | {'Price':<8}")
        print("-" * 65)
        for book in books_list:
            # UUID는 길기 때문에 앞 8자리만 표시
            book_id_short = str(book[0])[:8] + "..."
            title_val = book[1]
            price_val = book[2]
            print(f"{book_id_short:<38} | {title_val:<15} | {price_val:<8,}")
    else:
        print("조회된 도서 데이터가 없습니다.")
    print("-" * 65)


if __name__ == '__main__':
    # 메인 실행 가이드: 테이블 생성 -> 데이터 삽입 -> 업데이트 -> 삭제 -> 최종 확인 순으로 실행합니다.
    print("=====================================================")
    print("--- [문제 1] books 테이블 CRUD 프로세스 시작 (초기화) ---")
    print("=====================================================")
    
    # 1. 테이블 생성 (기존 테이블 삭제 후 재생성)
    create_books_table()

    # 2. 테스트 데이터 삽입
    insert_books()

    # 3. 업데이트 전 상태 확인 (Initial State)
    print("\n[업데이트 및 삭제 전 전체 도서 목록 확인]")
    all_books_initial = get_all_books()
    print_books("초기 삽입된 전체 도서", all_books_initial)
    
    # 4. 데이터 업데이트 실행 (두 번째 도서 가격 27000으로 수정)
    print("\n[데이터 업데이트 실행]")
    update_second_book_price()

    # 5. 삭제 전 상태 확인 (After Update)
    print("\n[삭제 전 전체 도서 목록 확인]")
    all_books_before_delete = get_all_books()
    print_books("업데이트 후 전체 도서 (삭제 대상 포함)", all_books_before_delete)

    # 6. 데이터 삭제 실행 (세 번째 도서 삭제)
    print("\n[데이터 삭제 실행]")
    delete_third_book()

    # 7. 최종 상태 확인 (After Delete)
    print("\n[최종 전체 도서 목록 확인]")
    all_books_final = get_all_books()
    print_books("삭제 후 최종 도서", all_books_final)

    print("=====================================================")
    print("--- 모든 CRUD 프로세스 완료 ---")
    print("=====================================================")