from presentation_layer.main_menu import Menu

class CourseMenu(Menu):
    def render(self):
        print("""
=== Course Menu ===
1) Create Course
2) View Courses
3) Update Course
4) Delete Course
5) View Student Roster by Course
0) Back
""")
        user_input = input("Select an option: ").lower()
        match user_input:
            case "1":
                self.create_course()
            case "2":
                self.view_courses()
            case "3":
                self.update_course()
            case "4":
                self.delete_course()
            case "5":
                self.view_course_students()
            case "0":
                from presentation_layer.main_menu import MainMenu
                self.terminal.navigate(MainMenu(self.terminal))
            case _:
                print("Invalid choice")

    def create_course(self):
        print("\n=== Create New Course ===")
        name = self.format_name(input("Enter course name: "))
        professor_id = int(input("Enter professor ID: "))
        professor = self.terminal.professor_service.get_professor_by_id(professor_id)

        try:
            print(f"\nCreating course as \n Name: {name} \n Professor: {professor['first_name']} {professor['last_name']}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.course_service.create_new_course(
                    name, professor_id
                )
                print("Course created successfully!")
            else:
                print("Course creation canceled.")
                self.terminal.navigate(CourseMenu(self.terminal))
        except Exception as e:
            print(f"Error creating course: {e}")
        finally:
            print("\nReturning to course menu...")

        self.terminal.navigate(CourseMenu(self.terminal))

    def view_courses(self):
        print("\n=== All Courses ===")

        try:
            courses = self.terminal.course_service.get_all_courses()
            if not courses:
                print("No courses found.")
            for c in courses:
                print(f"{c['id']}: Name: {c['name']} | Professor ID: {c['professor_id']}")
        except Exception as e:
            print(f"Error retrieving courses: {e}")
        finally:
            print("\nReturning to course menu...")

        self.terminal.navigate(CourseMenu(self.terminal))

    def update_course(self):
        print("\n=== Update Course ===")

        try:
            course_id = int(input("Enter course ID: "))
            name = self.format_name(input("New course name: "))
            professor_id = int(input("New professor ID: "))

            print(f"\nUpdating course as \n Name: {name} \n Professor ID: {professor_id}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.course_service.update_existing_course(
                    course_id, name, professor_id
                )
                print("Course updated successfully!")
            else:
                print("Course update canceled.")
                self.terminal.navigate(CourseMenu(self.terminal))
        except Exception as e:
            print(f"Error updating course: {e}")

        self.terminal.navigate(CourseMenu(self.terminal))

    def delete_course(self):
        print("\n=== Delete Course ===")

        try:
            course_id = int(input("Enter course ID: "))
            course = self.terminal.course_service.get_course_by_id(course_id)
            print(f"\nDeleting course: {course['name']}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.course_service.delete_existing_course(course_id)
                print("Course deleted successfully!")
            else:
                print("Course deletion canceled.")
                self.terminal.navigate(CourseMenu(self.terminal))
        except Exception as e:
            print(f"Error deleting course: {e}")

        self.terminal.navigate(CourseMenu(self.terminal))

    def view_course_students(self):
        print("\n=== View Student Roster by Course ===")

        try:
            course_id = int(input("Enter course ID: "))
            students = self.terminal.course_service.get_course_students(course_id)
            if not students:
                print("No students found for this course.")
            for s in students:
                print(f"{s['id']}: {s['first_name']} {s['last_name']} | {s['email']}")
        except Exception as e:
            print(f"Error retrieving course students: {e}")

        self.terminal.navigate(CourseMenu(self.terminal))
