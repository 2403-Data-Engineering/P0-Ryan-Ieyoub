from data_layer.connection_manager import get_connection

def get_all_courses():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()

def create_course(name: str, professor_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO courses (name, professor_id) VALUES (%s, %s)",
            [name, professor_id]
        )
        conn.commit()

def delete_course(id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = %s", [id])
        conn.commit()

def update_course(id: int, name: str, professor_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE courses SET name = %s, professor_id = %s WHERE id = %s",
            [name, professor_id, id]
        )
        conn.commit()

def get_students_by_course(course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT s.id, s.first_name, s.last_name, s.email
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            WHERE e.course_id = %s
        """, [course_id])
        return cursor.fetchall()
    
def get_course_by_id(course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses WHERE id = %s", [course_id])
        return cursor.fetchone()