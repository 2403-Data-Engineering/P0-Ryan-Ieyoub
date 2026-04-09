from abc import abstractmethod
import re
from presentation_layer.terminal import Terminal

class Menu:
    def __init__(self, terminal: Terminal):
        self.terminal:Terminal = terminal

    @abstractmethod
    def render() -> None:
        pass

    def get_valid_email(self):
        while True:
            email = input("Enter email: ").strip()
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                return email
            else:
                print("Invalid email format. Please try again.")

    def format_name(self, value: str) -> str:
        return value.strip().capitalize()

    def confirm_changes(self):
        print("""\n
Submit Changes or Cancel
1) Submit
2) Cancel
""")
        user_input = input("Select an option: ").lower()
        match user_input:
            case "1":
                return True
            case "2":
                return False
            case _:
                print("Invalid choice")
                return self.confirm_changes()
            
     