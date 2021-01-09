# ------------------------------------------------#
from ui import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtCore import pyqtSlot, QTimer

# Global definitions -----------------------------#
MINUTE = 1
active = False
reps = 0
# ------------------------------------------------#

def reset_timer():
    global reps
    global active
    global ui
    reps = 0
    active = False
    ui.time_label.setText("00:00")
    ui.title_label.setText("Reset")

def start_timer():
    global reps
    global active
    global ui
    if active is False:
        active = True
        reps += 1
        if reps <= 8:
            if reps % 8 == 0:
                ui.title_label.setText("Long Rest")
                count_down(20 * MINUTE)
            elif reps % 2 == 0:
                ui.title_label.setText("Short Rest")
                count_down(5 * MINUTE)
            else:
                ui.title_label.setText("Working")
                count_down(25 * MINUTE)
        else:
            ui.time_label.setText("Done")
            active = False


# -------------------------
@pyqtSlot()
def count_down(count):
    global active
    global ui
    if active is True:
        count -= 1
        mins = count // 60
        secs = count % 60
        print(f"{mins}:{secs:02}")
        ui.time_label.setText(f"{mins}:{secs:02}")
        if count >= 0:
            QTimer.singleShot(1000, lambda: count_down(count))
        else:
            start_timer()

@pyqtSlot()
def on_start_button():
    start_timer()

@pyqtSlot()
def on_reset_button():
    reset_timer()

# Main --------------------------------------------#
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # Button Connections --------------------------#
    ui.start_button.clicked.connect(on_start_button)
    ui.reset_button.clicked.connect(on_reset_button)

    sys.exit(app.exec_())
