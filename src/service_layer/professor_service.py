import os
import webbrowser
from data_layer.professor_dao import (
    get_all_professors,
    create_professor,
    update_professor,
    delete_professor,
    get_courses_by_professor,
    get_professor_by_id   
)
from service_layer.course_service import CourseService

class ProfessorService:
    def get_all_professors(self):
        return get_all_professors()
    
    def get_professor_by_id(self, id):
        return get_professor_by_id(id)

    def create_new_professor(self, first_name, last_name, email, dept):
        create_professor(first_name, last_name, email, dept)

    def update_existing_professor(self, id, first_name, last_name, email, dept):
        update_professor(id, first_name, last_name, email, dept)

    def delete_existing_professor(self, id):
        delete_professor(id)

    def generate_professor_report(self, professor_id: int):
        professor = self.get_professor_by_id(professor_id)
        courses = get_courses_by_professor(professor_id)
        course_service = CourseService()

        html = f"""
        <html>
        <head>
            <title>Professor Report</title>
        </head>
        <body>
            <h1>Professor Report</h1>
            <h2>{professor['first_name']} {professor['last_name']}</h2>
            <p>Email: {professor['email']}</p>

            <h3>Courses Teaching</h3>
            <ul>
        """

        for c in courses:
            html += f"<li>{c['name']}"
            students = course_service.get_course_students(c['id'])
            if students:
                html += "<ul>"
                for s in students:
                    html += f"<li>{s['first_name']} {s['last_name']}</li>"
                html += "</ul>"
            else:
                html += " (No students enrolled)"
            html += "</li>"

        html += """
            </ul>
        </body>
        </html>
        """

        file_name = f"{professor_id}.html"
        with open(file_name, "w") as f:
            f.write(html)
            
        webbrowser.open_new_tab(os.path.abspath(file_name))

        return file_name