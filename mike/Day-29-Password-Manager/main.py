# ---------------------------- IMPORTS
from random import randint, choices, shuffle
from pass_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import sys

# ---------------------------- Globals and Constants
ALLOWED_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALLOWED_NUMBERS= "1234567890"
ALLOWED_SYMBOLS = "!&%_+="
PROHIBITED_CHARS = ",\|/^~'`{}[];:.*#@"
password_file = "password.txt"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    """Generate a simple password using predefined datasets."""
    global ALLOWED_LETTERS
    global ALLOWED_NUMBERS
    global ALLOWED_SYMBOLS

    n_letters = 12
    n_numbers = 5
    n_symbols = 3
    letters = choices(population=ALLOWED_LETTERS, k=n_letters)
    numbers = choices(population=ALLOWED_NUMBERS, k=n_numbers)
    symbols = choices(population=ALLOWED_SYMBOLS, k=n_symbols)
    all_chars = letters + numbers + symbols
    shuffle(all_chars)
    return "".join(all_chars)

def verify_password(password: str) -> bool:
    for char in password:
        print("Char is :", char)
        if char in PROHIBITED_CHARS:
            return False
    else:
        return True

def update_password_text():
    global ui
    the_password = gen_password()
    ui.password_edit.setText(the_password)

def save_data():
    global ui
    if verify_password(ui.password_edit.text()):
        the_line = ui.website_edit.text() + ","
        the_line += ui.email_edit.text() + ","
        the_line += ui.password_edit.text() + "\n"
        print(the_line)
        with open(password_file, "a") as file_handle:
            file_handle.write(the_line)
    else:
        print("Prohibited characters in password, entry not saved")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setMaximumSize(646, 214)   # goes here because will be lost if set in ui.py

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.generate_button.clicked.connect(update_password_text)
ui.add_to_file_button.clicked.connect(save_data)

MainWindow.show()
sys.exit(app.exec_())