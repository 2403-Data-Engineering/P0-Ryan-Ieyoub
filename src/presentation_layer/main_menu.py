from presentation_layer.menu import Menu

class MainMenu(Menu):
    def render(self) -> None:
        print("""
===========================
Welcome
1) Student Operations
2) Professor Operations
3) Course Operations
0) Quit
        """)
    
        user_input: str = input().lower()
        match user_input:
            case "1":
                from presentation_layer.student_menu import StudentMenu
                self.terminal.navigate(StudentMenu(self.terminal)) 
            case "2":
                from presentation_layer.professor_menu import ProfessorMenu
                self.terminal.navigate(ProfessorMenu(self.terminal))
            case "3":
                from presentation_layer.course_menu import CourseMenu
                self.terminal.navigate(CourseMenu(self.terminal))
            case "0":
                self.terminal.quit()

