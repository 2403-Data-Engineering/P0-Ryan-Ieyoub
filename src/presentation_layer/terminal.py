class Terminal:
    def __init__(self, student_service, professor_service, course_service):
        from presentation_layer.main_menu import MainMenu

        self.student_service = student_service
        self.professor_service = professor_service
        self.course_service = course_service

        self.current_menu = MainMenu(self)
        self.running = True

    def navigate(self, menu):
        self.current_menu = menu

    def exit(self):
        self.running = False
        print("Exiting...")

    def run(self):
        while self.running:
            self.current_menu.render()