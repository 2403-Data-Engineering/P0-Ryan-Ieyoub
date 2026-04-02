from data_layer.models import Student

class Menu:
    def __init__(self, terminal: Terminal):
        self.terminal:Terminal = terminal

    @abstractmethod
    def render() -> None:
        pass

class MainMenu(Menu):
    def render(self) -> None:
        print("""
===========================
Welcome to uRevature Admin
1) Create new student
2) Create new professor
3) Create new class
4) Enroll student in class
5) Run report
Q) Quit
        """)
    
        user_input: str = input().lower()
        match user_input:
            case "1":
                self.terminal.navigate(StudentMenu(self.terminal)) 
            case "2":
                self.terminal.navigate(ProfessorMenu(self.terminal))
            case "3":
                self.terminal.navigate(CourseMenu(self.terminal))
            case "4":
                print("TODO: IMPLEMENT ME")
            case "5":
                print("TODO: IMPLEMENT ME")
            case "b":
                self.terminal.quit()

class StudentMenu(Menu):
    def render(self):
        print("""
=== Student Menu ===
1) Create Student
2) View Students
3) Update Student
4) Delete Student
B) Back
""")
    user_input: str = input().lower()
    match user_input:
            case "1":
                self.create_student()
            case "2":
                self.view_students()
            case "3":
                self.update_student()
            case "4":
                self.delete_student()
            case "b":
                self.terminal.navigate(MainMenu(self.terminal))
            case _:
                print("Invalid choice")
    
    def create_student(self):
        print("\n=== Create New Student ===")

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        major = input("Enter major: ")
        email = input("Enter email: ")
        year = input("Enter year: ")

        try:
            self.terminal.student_service.add_student(
                first_name, last_name, major, email, year
            )
            print("\nStudent created successfully!")
        except Exception as e:
            print("Exception. Please try again")
        finally:
            print("\nReturning to student menu...")

        self.terminal.navigate(StudentMenu(self.terminal))
    
    def view_students(self):
        print("\n=== All Students ===")

        try:
            students = self.terminal.student_service.get_all_students()
            for s in students:
                print(f"{s.id}: {s.first_name} {s.last_name} | {s.major} | {s.year}")
        except Exception:
            print("Error retrieving students")
        finally:
            print("\nReturning to student menu...")

        self.terminal.navigate(StudentMenu(self.terminal))
    
    def update_student(self):
        print("\n=== Update Student ===")

        student_id = input("Enter student ID: ")
        first_name = input("New first name: ")
        last_name = input("New last name: ")
        major = input("New major: ")
        email = input("New email: ")
        year = input("New year: ")

        try:
            self.terminal.student_service.update_student(
                student_id, first_name, last_name, major, email, year
            )
            print("Student updated successfully!")
        except Exception:
            print("Error updating student")

        self.terminal.navigate(StudentMenu(self.terminal))

    def delete_student(self):
        print("\n=== Delete Student ===")

        student_id = input("Enter student ID: ")

        try:
            self.terminal.student_service.delete_student(student_id)
            print("Student deleted successfully!")
        except Exception:
            print("Error deleting student")

        self.terminal.navigate(StudentMenu(self.terminal))

class ProfessorMenu(Menu):
    def render(self):
        print("""
=== Professor Menu ===
1) Create Professor
2) View Professors
3) Update Professor
4) Delete Professor
B) Back
""")
    user_input: str = input().lower()
    match user_input:
        case "1":
            self.create_professor()
        case "2":
            self.view_professors()
        case "3":
            self.update_professor()
        case "4":
            self.delete_professor()
        case "b":
            self.terminal.navigate(MainMenu(self.terminal))
        case _:
            print("Invalid choice")

    def create_professor(self):
        print("\n=== Create New Professor ===")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")

        try:
            self.terminal.professor_service.add_professor(
                first_name, last_name, email
            )
            print("Professor created successfully!")
        except Exception as e:
            print(f"Exception. Please try again")
        finally:
            print("\nReturning to professor menu...")

        self.terminal.navigate(ProfessorMenu(self.terminal))
    
    def view_professors(self):
        print("\n=== All Professors ===")

        try:
            professors = self.terminal.professor_service.get_all_professors()
            for p in professors:
                print(f"{p.id}: {p.first_name} {p.last_name} | {p.email}")
        except Exception:
            print("Error retrieving professors")
        finally:
            print("\nReturning to professor menu...")

        self.terminal.navigate(ProfessorMenu(self.terminal))

    def update_professor(self):
        print("\n=== Update Professor ===")

        professor_id = input("Enter professor ID: ")
        first_name = input("New first name: ")
        last_name = input("New last name: ")
        email = input("New email: ")

        try:
            self.terminal.professor_service.update_professor(
                professor_id, first_name, last_name, email
            )
            print("Professor updated successfully!")
        except Exception:
            print("Error updating professor")

        self.terminal.navigate(ProfessorMenu(self.terminal))

    def delete_professor(self):
        print("\n=== Delete Professor ===")

        professor_id = input("Enter professor ID: ")

        try:
            self.terminal.professor_service.delete_professor(professor_id)
            print("Professor deleted successfully!")
        except Exception:
            print("Error deleting professor")

        self.terminal.navigate(ProfessorMenu(self.terminal))

class CourseMenu(Menu):
    def render(self):
        print("""
=== Course Menu ===
1) Create Course
2) View Courses
3) Update Course
4) Delete Course
B) Back
""")
    user_input: str = input().lower()
    match user_input:
        case "1":
            self.create_course()
        case "2":
            self.view_courses()
        case "3":
            self.update_course()
        case "4":
            self.delete_course()
        case "b":
            self.terminal.navigate(MainMenu(self.terminal))
        case _:
            print("Invalid choice")

    def create_course(self):
        print("\n=== Create New Course ===")
        name = input("Enter course name: ")
        p_id = input("Enter professor ID: ")

        try:
            self.terminal.course_service.add_course(
                name, p_id
            )
            print("Course created successfully!")
        except Exception as e:
            print(f"Exception. Please try again")
        finally:
            print("\nReturning to course menu...")
        self.terminal.navigate(CourseMenu(self.terminal))

    def view_courses(self):
        print("\n=== All Courses ===")

        try:
            courses = self.terminal.course_service.get_all_courses()
            for c in courses:
                print(f"{c.id}: {c.name} | Professor ID: {c.professor_id}")
        except Exception:
            print("Error retrieving courses")
        finally:
            print("\nReturning to course menu...")

        self.terminal.navigate(CourseMenu(self.terminal))

    def update_course(self):
        print("\n=== Update Course ===")

        course_id = input("Enter course ID: ")
        name = input("New course name: ")
        professor_id = input("New professor ID: ")

        try:
            self.terminal.course_service.update_course(
                course_id, name, professor_id
            )
            print("Course updated successfully!")
        except Exception:
            print("Error updating course")

        self.terminal.navigate(CourseMenu(self.terminal))

    def delete_course(self):
        print("\n=== Delete Course ===")

        course_id = input("Enter course ID: ")

        try:
            self.terminal.course_service.delete_course(course_id)
            print("Course deleted successfully!")
        except Exception:
            print("Error deleting course")

        self.terminal.navigate(CourseMenu(self.terminal))
