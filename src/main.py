from presentation_layer.terminal import Terminal
from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.course_service import CourseService


def main():
    student_service = StudentService()
    professor_service = ProfessorService()
    course_service = CourseService()

    terminal = Terminal(
        student_service,
        professor_service,
        course_service
    )

    terminal.run()

if __name__ == "__main__":
    main()
