# ---------------------------- IMPORTS
from random import randint, choices, shuffle
from pass_ui import Ui_MainWindow
from confirm_dialog import Ui_Dialog
from error_dialog import Ui_error_dialog
from PyQt6 import QtWidgets, QtCore
import sys

# ---------------------------- Globals and Constants
ALLOWED_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALLOWED_NUMBERS = "1234567890"
ALLOWED_SYMBOLS = "!&%_+="
PROHIBITED_CHARS = ",\|/^~'`{}[];:.*#@"
password_file = "password.txt"
error_char: str


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
# end def


def verify_password(password: str) -> bool:
    global error_char
    if len(password.strip()) == 0:
        error_no_entry("Error: No password entered")
        return False

    for char in password:
        if char in PROHIBITED_CHARS:
            error_char = char
            error_no_entry(f"Error: illegal character '{char}'\nin password")
            return False

    else:
        return True
# end def


def update_password_text():
    global ui
    the_password = gen_password()
    ui.password_edit.setText(the_password)
# end def


def verify_username() -> bool:
    global ui
    text = ui.email_edit.text().strip()
    if len(text) == 0:
        error_no_entry("Error: No username/email entered")
        return False
    return True
# end def


def verify_website() -> bool:
    global ui
    text = ui.website_edit.text().strip()
    if len(text) == 0:
        error_no_entry("Error: No website entered")
        return False
    return True
# end def


def error_no_entry(err_text: str):
    global err_ui
    global Error_dialog
    err_ui.error_dialog_label.setText(err_text)
    Error_dialog.show()
# end def


def save_data():
    global ui
    global dia_ui
    global Dialog

    if verify_website() and verify_username() and verify_password(ui.password_edit.text()):
        # Step 1 : write the line to the password file
        the_line = f"{ui.website_edit.text()}," \
                   f"{ui.email_edit.text()}," \
                   f"{ui.password_edit.text()}\n"
        with open(password_file, "a") as file_handle:
            file_handle.write(the_line)

        # Step 2 : display text in the dialog  (and show Dialog)
        the_label_text = "Data written to file:\n\n" \
                         f"{ui.website_edit.text()}\n\n" \
                         f"{ui.email_edit.text()}\n\n" \
                         f"{ui.password_edit.text()}"
        dia_ui.dialog_label.setText(the_label_text)
        Dialog.show()
    else:
        print("Prohibited characters in password, entry not saved")
# end def


# instantiate app
app = QtWidgets.QApplication(sys.argv)

# main window setup
MainWindow = QtWidgets.QMainWindow()
MainWindow.setMaximumSize(646, 214)  # goes here because will be lost if set in ui.py
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.generate_button.clicked.connect(update_password_text)
ui.add_to_file_button.clicked.connect(save_data)

# dialog setup
Dialog = QtWidgets.QDialog()
dia_ui = Ui_Dialog()
dia_ui.setupUi(Dialog)
dia_ui.dialog_button.clicked.connect(Dialog.hide)

Error_dialog = QtWidgets.QWidget()
err_ui = Ui_error_dialog()
err_ui.setupUi(Error_dialog)
err_ui.error_dialog_button.clicked.connect(Error_dialog.hide)

MainWindow.show()
sys.exit(app.exec())
