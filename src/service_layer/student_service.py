import os
import webbrowser
from data_layer.student_dao import (
    get_all_students,
    create_student,
    get_courses_by_student,
    update_student,
    delete_student,
    enroll_student,
    drop_student_from_course,
    get_student_by_id
)

class StudentService:
    def get_all_students(self):
        return get_all_students()

    def get_student_by_id(self, id):
        return get_student_by_id(id)

    def create_new_student(self, first_name, last_name, major, email, student_year):
        create_student(first_name, last_name, major, email, student_year)

    def update_existing_student(self, id, first_name, last_name, major, email, student_year):
        update_student(id, first_name, last_name, major, email, student_year)

    def delete_existing_student(self, id):
        delete_student(id)

    def enroll_student(self, student_id: int, course_id: int):
        enroll_student(student_id, course_id)

    def get_student_courses(self, student_id: int):
        return get_courses_by_student(student_id)
    
    def drop_student_from_course(self, student_id: int, course_id: int):
        drop_student_from_course(student_id, course_id)

    def generate_student_report(self, student_id: int):
        student = self.get_student_by_id(student_id)
        courses = self.get_student_courses(student_id)

        html = f"""
        <html>
        <head>
            <title>Student Report</title>
        </head>
        <body>
            <h1>Student Report</h1>
            <h2>{student['first_name']} {student['last_name']}</h2>

            <h3>Enrolled Courses</h3>
            <ul>
        """

        for c in courses:
            html += f"<li>{c['name']}</li>"

        html += """
            </ul>
        </body>
        </html>
        """

        file_name = f"{student_id}.html"
        with open(file_name, "w") as f:
            f.write(html)

        webbrowser.open_new_tab(os.path.abspath(file_name))
        
        return file_name