from db import get_pg_conn
from typing import Optional

def create_user(name: str, email: str) -> int:
    conn = get_pg_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (name, email))
            user_id = cursor.fetchone()[0]
            conn.commit()
            return user_id
    finally:
        conn.close()

def get_user(user_id: int) -> Optional[dict]:
    conn = get_pg_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            if user:
                return {"id": user[0], "name": user[1], "email": user[2]}
            return None
    finally:
        conn.close()
