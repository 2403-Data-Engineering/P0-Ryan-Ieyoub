import os
from presentation_layer.main_menu import Menu

class StudentMenu(Menu):
    def render(self):
        print("""
=== Student Menu ===
1) Create Student
2) View Students
3) Update Student
4) Delete Student
5) Enroll Student
6) View Student Schedule
7) Drop Student from Course
8) Generate Student Report
0) Back
""")
        user_input = input("Select an option: ").lower()
        match user_input:
            case "1":
                self.create_student()
            case "2":
                self.view_students()
            case "3":
                self.update_student()
            case "4":
                self.delete_student()
            case "5":
                self.enroll_student()
            case "6":
                self.view_student_schedule()
            case "7":
                self.drop_student_from_course()
            case "8":
                self.generate_student_report()
            case "0":
                from presentation_layer.main_menu import MainMenu
                self.terminal.navigate(MainMenu(self.terminal))
            case _:
                print("Invalid choice")

    def create_student(self):
        print("\n=== Create New Student ===")
        first_name = self.format_name(input("Enter first name: "))
        last_name = self.format_name(input("Enter last name: "))
        major = self.format_name(input("Enter major: "))
        email = self.get_valid_email()
        student_year = self.get_student_year()

        try:
            
            print(f"\nCreating student as \n Name: {first_name} {last_name} \n Major: {major} \n Email: {email} \n Year: {student_year}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.student_service.create_new_student(
                first_name, last_name, major, email, student_year
            )
                print("Student created successfully!")
                
            else:
                print("Student creation canceled.")
                self.terminal.navigate(StudentMenu(self.terminal))
        except Exception as e:
            print(f"Error creating student: {e}")
        finally:
            print("\nReturning to student menu...")

        self.terminal.navigate(StudentMenu(self.terminal))

    def view_students(self):
        print("\n=== All Students ===")

        try:
            students = self.terminal.student_service.get_all_students()
            if not students:
                print("No students found.")
            for s in students:
                print(f"{s['id']}: Name: {s['first_name']} {s['last_name']} | Major: {s['major']} | Email: {s['email']} | Year: {s['student_year']}")
        except Exception as e:
            print(f"Error retrieving students: {e}")
        finally:
            print("\nReturning to student menu...")

        self.terminal.navigate(StudentMenu(self.terminal))

    def update_student(self):
        print("\n=== Update Student ===")

        try:
            student_id = int(input("Enter student ID: "))
            first_name = self.format_name(input("Enter first name: "))
            last_name = self.format_name(input("Enter last name: "))
            major = self.format_name(input("Enter major: "))
            email = self.get_valid_email()
            student_year = self.get_student_year()

            
            print(f"\nUpdating student as \n Name: {first_name} {last_name} \n Major: {major} \n Email: {email} \n Year: {student_year}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.student_service.update_existing_student(
                    student_id, first_name, last_name, major, email, student_year
                )
                print("Student updated successfully!")
            else:
                print("Student update canceled.")
                self.terminal.navigate(StudentMenu(self.terminal))
        except Exception as e:
            print(f"Error updating student: {e}")

        self.terminal.navigate(StudentMenu(self.terminal))

    def delete_student(self):
        print("\n=== Delete Student ===")

        try:
            student_id = int(input("Enter student ID: "))
            student = self.terminal.student_service.get_student_by_id(student_id)
            print(f"\nDeleting student: {student['first_name']} {student['last_name']}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.student_service.delete_existing_student(student_id)
                print("Student deleted successfully!")
            else:
                print("Student deletion canceled.")
                self.terminal.navigate(StudentMenu(self.terminal))
        except Exception as e:
            print(f"Error deleting student: {e}")

        self.terminal.navigate(StudentMenu(self.terminal))

    def enroll_student(self):
        print("\n=== Enroll Student in Course ===")

        try:
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            student = self.terminal.student_service.get_student_by_id(student_id)
            course = self.terminal.course_service.get_course_by_id(course_id)
            print(f"\nEnrolling student: {student['first_name']} {student['last_name']} in course: {course['name']}")
            confirm = self.confirm_changes()

            if confirm:
                self.terminal.student_service.enroll_student(student_id, course_id)
                print("Student enrolled successfully!")
            else:
                print("Student enrollment canceled.")
                self.terminal.navigate(StudentMenu(self.terminal))
        except Exception as e:
            print(f"Error enrolling student: {e}")

        self.terminal.navigate(StudentMenu(self.terminal))
    
    def view_student_schedule(self):
        print("\n=== View Student Schedule ===")

        try:
            student_id = int(input("Enter student ID: "))
            courses = self.terminal.student_service.get_student_courses(student_id)
            if not courses:
                print("No courses found for this student.")
            for c in courses:
                print(f"{c['id']}: {c['name']}")
        except Exception as e:
            print(f"Error retrieving student schedule: {e}")

        self.terminal.navigate(StudentMenu(self.terminal))
    
    def drop_student_from_course(self):
        print("\n=== Drop Student from Course ===")
        try:
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            student = self.terminal.student_service.get_student_by_id(student_id)
            course = self.terminal.course_service.get_course_by_id(course_id)
            print(f"\nDropping student: {student['first_name']} {student['last_name']} from course: {course['name']}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.student_service.drop_student_from_course(student_id, course_id)
                print("Student dropped from course successfully!")
            else:
                print("Student drop canceled.")
                self.terminal.navigate(StudentMenu(self.terminal))
        except Exception as e:
            print(f"Error dropping student from course: {e}")

        self.terminal.navigate(StudentMenu(self.terminal))

    def generate_student_report(self):
        print("\n=== Generate Student Report ===")

        try:
            student_id = int(input("Enter student ID: "))
            file_name = self.terminal.student_service.generate_student_report(student_id)
            print(f"Report generated: {os.path.abspath(file_name)}")
        except Exception as e:
            print(f"Error generating report: {e}")

        self.terminal.navigate(StudentMenu(self.terminal))

    def get_student_year(self):
        print("""
            Select student year:
            1) Freshman
            2) Sophomore
            3) Junior
            4) Senior
            """)
        choice = input("Enter choice: ")
        match choice:
            case "1":
                return "Freshman"
            case "2":
                return "Sophomore"
            case "3":
                return "Junior"
            case "4":
                return "Senior"
            case _:
                print("Invalid choice")
                return self.get_student_year()
            
   