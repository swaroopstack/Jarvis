import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit


app = QApplication(sys.argv)

window = QWidget()
window.resize(700, 100)
window.setWindowTitle("JARVIS")

input_box = QLineEdit(window)
input_box.setPlaceholderText("What can I do for you?")
input_box.resize(600, 50)
input_box.move(50, 25)

window.show()

sys.exit(app.exec())