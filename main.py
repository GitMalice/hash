from PyQt5.uic import *
from PyQt5.QtWidgets import *
from panel import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("MyCoder")
        self.ui.show_button.clicked.connect(self.show_entry)
        self.ui.add_button.clicked.connect(self.add_entry)


    def add_entry(self):
        crypted = ""
        # print("add")
        entry = self.ui.line_str.text()
        user_key = self.ui.line_key.text()
        for letter in entry:
            new_value = ord(letter) + int(user_key)
            if new_value > 122:
                new_value = new_value - 25
            crypted += chr(new_value)
        self.ui.line_str.setText("")
        self.ui.line_key.setText("")
        with open("crypted_lines.txt", "a") as crypted_lines:
            crypted_lines.write(f"{entry} || {user_key} || {crypted}\n")

    def show_entry(self):
        with open("crypted_lines.txt", "r") as crypted_lines:
            content = crypted_lines.read()
            self.ui.bloc_text.setText(content)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
