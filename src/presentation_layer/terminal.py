from service_layer.student_service import StudentService

class Terminal:
    _instance = None

    def __init__(self, student_service: StudentService):
        from presentation_layer.menu import MainMenu
        self.current_menu = MainMenu(self)
        self.running = True
        self.student_service = student_service

    def navigate(self, menu: Menu):
        self.current_menu = menu

    def exit(self):
        self.running = False
        print("Exiting...")