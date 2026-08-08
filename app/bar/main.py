import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit

from launcher import launch_application, open_website, search_web


app = QApplication(sys.argv)

window = QWidget()
window.resize(700, 100)
window.setWindowTitle("JARVIS")

input_box = QLineEdit(window)
input_box.resize(600, 50)
input_box.move(50, 25)
input_box.setPlaceholderText("What can I do for you?")


def handle_command():
    command = input_box.text().lower().strip()

    if command.startswith("search "):
        query = command[7:]
        search_web(query)

    elif command == "github":
        open_website("https://github.com")

    elif command == "youtube":
        open_website("https://youtube.com")

    elif command == "google":
        open_website("https://google.com")

    elif launch_application(command):
        print(f"Opening {command}...")

    else:
        print(f"I don't know how to handle: {command}")

    input_box.clear()


input_box.returnPressed.connect(handle_command)

window.show()

sys.exit(app.exec())