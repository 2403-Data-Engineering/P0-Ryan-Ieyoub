import os
from presentation_layer.main_menu import Menu

class ProfessorMenu(Menu):
    def render(self):
        print("""
=== Professor Menu ===
1) Create Professor
2) View Professors
3) Update Professor
4) Delete Professor
5) Generate Professor Report
0) Back
""")
        user_input = input("Select an option: ").lower()
        match user_input:
            case "1":
                self.create_professor()
            case "2":
                self.view_professors()
            case "3":
                self.update_professor()
            case "4":
                self.delete_professor()
            case "5":
                self.generate_professor_report()
            case "0":
                from presentation_layer.main_menu import MainMenu
                self.terminal.navigate(MainMenu(self.terminal))
            case _:
                print("Invalid choice")

    def create_professor(self):
        print("\n=== Create New Professor ===")
        first_name = self.format_name(input("Enter first name: "))
        last_name = self.format_name(input("Enter last name: "))
        email = self.get_valid_email()
        dept = self.format_name(input("Enter department: "))

        try:
            self.terminal.professor_service.create_new_professor(
                first_name, last_name, email, dept
            )
            print(f"\nCreating professor as \n Name: {first_name} {last_name} \n Email: {email} \n Department: {dept}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.professor_service.create_new_professor(
                    first_name, last_name, email, dept
                )
                print("Professor created successfully!")
            else:
                print("Professor creation canceled.")
                self.terminal.navigate(ProfessorMenu(self.terminal))
        except Exception as e:
            print(f"Error creating professor: {e}")
        finally:
            print("\nReturning to professor menu...")

        self.terminal.navigate(ProfessorMenu(self.terminal))

    def view_professors(self):
        print("\n=== All Professors ===")

        try:
            professors = self.terminal.professor_service.get_all_professors()
            if not professors:
                print("No professors found.")
            for p in professors:
                print(f"{p['id']}: Name: {p['first_name']} {p['last_name']} | Email: {p['email']} | Department: {p['dept']}")
        except Exception as e:
            print(f"Error retrieving professors: {e}")
        finally:
            print("\nReturning to professor menu...")

        self.terminal.navigate(ProfessorMenu(self.terminal))

    def update_professor(self):
        print("\n=== Update Professor ===")

        try:
            professor_id = int(input("Enter professor ID: "))
            first_name = self.format_name(input("New first name: "))
            last_name = self.format_name(input("New last name: "))
            email = self.get_valid_email()
            dept = self.format_name(input("New department: "))

            print(f"\nUpdating professor as \n Name: {first_name} {last_name} \n Email: {email} \n Department: {dept}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.professor_service.update_existing_professor(
                    professor_id, first_name, last_name, email, dept
                )
                print("Professor updated successfully!")
            else:
                print("Professor update canceled.")
                self.terminal.navigate(ProfessorMenu(self.terminal))
        except Exception as e:
            print(f"Error updating professor: {e}")

        self.terminal.navigate(ProfessorMenu(self.terminal))

    def delete_professor(self):
        print("\n=== Delete Professor ===")

        try:
            professor_id = int(input("Enter professor ID: "))
            professor = self.terminal.professor_service.get_professor_by_id(professor_id)
            print(f"\nDeleting professor: {professor['first_name']} {professor['last_name']}")
            confirm = self.confirm_changes()
            if confirm:
                self.terminal.professor_service.delete_existing_professor(professor_id)
                print("Professor deleted successfully!")
            else:
                print("Professor deletion canceled.")
                self.terminal.navigate(ProfessorMenu(self.terminal))
        except Exception as e:
            print(f"Error deleting professor: {e}")

        self.terminal.navigate(ProfessorMenu(self.terminal))

    def generate_professor_report(self):
        print("\n=== Generate Professor Report ===")

        try:
            professor_id = int(input("Enter professor ID: "))
            file_name = self.terminal.professor_service.generate_professor_report(professor_id)
            print(f"Report generated: {os.path.abspath(file_name)}")
        except Exception as e:
            print(f"Error generating report: {e}")

        self.terminal.navigate(ProfessorMenu(self.terminal))