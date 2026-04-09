from data_layer.connection_manager import get_connection


def get_student_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", [id])
        return cursor.fetchone()

def get_all_students():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    
def create_student(first_name: str, last_name: str, major: str, email: str, student_year: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (first_name, last_name, major, email, student_year) VALUES (%s, %s, %s, %s, %s)",
            [first_name, last_name, major, email, student_year]
        )
        conn.commit()

def delete_student(id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", [id])
        conn.commit()

def update_student(id: int, first_name: str, last_name: str, major: str, email: str, student_year: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET first_name = %s, last_name = %s, major = %s, email = %s, student_year = %s WHERE id = %s",
            [first_name, last_name, major, email, student_year, id]
        )
        conn.commit()

def enroll_student(student_id: int, course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
            [student_id, course_id]
        )
        conn.commit()

def drop_student_from_course(student_id: int, course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM enrollments WHERE student_id = %s AND course_id = %s",
            [student_id, course_id]
        )
        conn.commit()

def get_courses_by_student(student_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT c.id, c.name
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.student_id = %s
        """, [student_id])
        return cursor.fetchall()