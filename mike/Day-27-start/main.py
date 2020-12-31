import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()
input = tkinter.Entry()
input.pack()

def button_clicked():
    the_value = int(input.get()) * 1.6
    my_label["text"] = the_value

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()
