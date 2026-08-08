import sys
import keyboard

from PySide6.QtCore import QObject, Signal, Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit

from launcher import launch_application, open_website, search_web


class HotkeySignal(QObject):
    triggered = Signal()


app = QApplication(sys.argv)

window = QWidget()
window.resize(700, 100)
window.setWindowTitle("JARVIS")

window.setWindowFlags(
    Qt.WindowType.Window |
    Qt.WindowType.WindowStaysOnTopHint
)

input_box = QLineEdit(window)
input_box.resize(600, 50)
input_box.move(50, 25)
input_box.setPlaceholderText("What can I do for you?")


def handle_command():
    command = input_box.text().lower().strip()

    if not command:
        return

    if command.startswith("search "):
        query = command[7:]
        search_web(query)

    elif "." in command:
        open_website(f"https://{command}")

    elif launch_application(command):
        print(f"Opening {command}...")

    else:
        open_website(f"https://www.{command}.com")

    input_box.clear()


def show_jarvis():
    window.showNormal()
    window.raise_()
    window.activateWindow()

    QTimer.singleShot(
        100,
        input_box.setFocus
    )


hotkey_signal = HotkeySignal()

hotkey_signal.triggered.connect(show_jarvis)

keyboard.add_hotkey(
    "windows+j",
    hotkey_signal.triggered.emit
)

input_box.returnPressed.connect(handle_command)

window.hide()

sys.exit(app.exec())