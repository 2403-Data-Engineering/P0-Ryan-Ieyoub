from data_layer.connection_manager import get_connection

def get_professor_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors WHERE id = %s", [id])
        return cursor.fetchone()

def get_all_professors():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors")
        return cursor.fetchall()

def create_professor(first_name: str, last_name: str, email: str, dept: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO professors (first_name, last_name, email, dept) VALUES (%s, %s, %s, %s)",
            [first_name, last_name, email, dept]
        )
        conn.commit()

def delete_professor(id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM professors WHERE id = %s", [id])
        conn.commit()

def update_professor(id: int, first_name: str, last_name: str, email: str, dept: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE professors SET first_name = %s, last_name = %s, email = %s, dept= %s WHERE id = %s",
            [first_name, last_name, email, dept, id]
        )
        conn.commit()

def get_courses_by_professor(professor_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, name
            FROM courses
            WHERE professor_id = %s
        """, [professor_id])
        return cursor.fetchall()