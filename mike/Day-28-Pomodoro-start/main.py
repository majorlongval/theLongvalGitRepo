# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
MINUTE = 60

# ---------------------------- GLOBAL VARS ------------------------------- #
reps = 0
active = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global active
    global title_label
    global timer_text
    reps = 0
    active = False
    canvas.itemconfig(timer_text, text="00:00")
    title_label.configure(text="Pomodoro Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global active
    global title_label
    active = True
    reps += 1
    print("Reps:", reps)
    if reps <= 8:
        if reps % 8 == 0:
            title_label.configure(text="   Long Rest  ")
            count_down(20 * MINUTE)
        elif reps % 2 == 0:
            title_label.configure(text="  Short Rest  ")

            count_down(10 * MINUTE)
        else:
            title_label.configure(text="   Working    ")
            count_down(25 * MINUTE)
    else:
        title_label.configure(text="  ** Done **  ")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global active
    global canvas
    if active is True:
        mins = count // 60
        secs = count % 60
        canvas.itemconfig(timer_text, text=f"{mins}:{secs:02}")
        count -= 1
        if count >= 0:
            window.after(1000, count_down, count)
        else:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Pomodoro Timer", fg=GREEN,
                    bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 132, text="00:00",
                                font=(FONT_NAME, 36, "bold"), fill=YELLOW)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", fg=GREEN, bg=YELLOW,
                      font=(FONT_NAME, 20, "bold"),
                      highlightthickness=0,
                      command=start_timer)

start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=GREEN, bg=YELLOW,
                      font=(FONT_NAME, 20, "bold"),
                      highlightthickness=0,
                      command=reset_timer)

reset_button.grid(column=2, row=2)

check_label = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 60, "bold"))
check_label.grid(column=1, row=2)

# ---------------------------- MAIN ------------------------------- #
window.mainloop()
