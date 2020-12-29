""""Just for fun I reimplemented the Pomodoro timer from Udemy 100 days of Python
(Day 28) in PyQt5 as a learning experience.
It's still a little buggy, but works mostly.
Mike mlongval@gmail.com
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSlot, QTimer
import PyQt5

# Constants -------------------------
MINUTE = 60         # setting this to 1 will allow for faster countdowns for debugging

# Globals -------------------------
timer_label: QLabel
the_window: QWidget
reps = 0
active = False


# -------------------------
@pyqtSlot()
def reset_timer():
    global reps
    global active
    global timer_label
    global the_window
    reps = 0
    active = False
    timer_label.setText("00:00")
    the_window.setWindowTitle("Pomodoro Timer")


# -------------------------
@pyqtSlot()
def start_timer():
    global reps
    global active
    global the_window
    active = True
    reps += 1
    if reps <= 8:
        if reps % 8 == 0:
            the_window.setWindowTitle("Long Rest")
            count_down(20 * MINUTE)
        elif reps % 2 == 0:
            the_window.setWindowTitle("Short Rest")
            count_down(5 * MINUTE)
        else:
            the_window.setWindowTitle("Working")
            count_down(25 * MINUTE)
    else:
        the_window.setWindowTitle("Done")


# -------------------------
@pyqtSlot()
def count_down(count):
    global timer_label
    global active
    if active is True:
        mins = count // 60
        secs = count % 60
        timer_label.setText(f"{mins}:{secs:02}")
        count -= 1
        if count >= 0:
            QTimer.singleShot(1000, lambda: count_down(count))
        else:
            start_timer()
    else:
        start_timer()


# Main Loop definition -------------------------
def main_loop():
    global timer_label
    global the_window
    app = QApplication(sys.argv)
    # main window
    the_window = QWidget()
    the_window.setGeometry(0, 0, 640, 400)
    the_window.setWindowTitle("Pomodoro Timer")

    # this sets the background picture which is the Tomato from the
    # Pomodoro lesson that was built initially with Tkinter.
    the_pixmap = QPixmap('tomato.png')
    background_label = QLabel(the_window)
    background_label.setPixmap(the_pixmap)
    background_label.move(220, 80)

    # font definitions
    the_font_large = QFont("Courier", 40, PyQt5.QtGui.QFont.Bold)
    the_font_small = QFont("Courier", 20, PyQt5.QtGui.QFont.Bold)

    # timer label
    timer_label = QLabel(the_window)
    timer_label.setText("00:00")
    timer_label.setFont(the_font_large)
    timer_label.move(270, 190)

    # start button
    start_button = QPushButton(the_window)
    start_button.setFont(the_font_small)
    start_button.setText("Start")
    start_button.setFont(the_font_small)
    start_button.move(120, 190)
    start_button.clicked.connect(lambda: count_down(25))

    # reset button
    reset_button = QPushButton(the_window)
    reset_button.setFont(the_font_small)
    reset_button.setText("Reset")
    reset_button.move(420, 190)
    reset_button.clicked.connect(reset_timer)

    the_window.show()
    sys.exit(app.exec_())
# end def main_loop


# Run Main Loop -------------------------
if __name__ == '__main__':
    main_loop()
