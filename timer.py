#программа таймер

from tkinter import *
import time

root = Tk()
root.title("Timer")
f = Frame()
f.pack()

time_var = StringVar()
time_label = Label(f, textvariable=time_var, font="Courier 60",
                   bg="lightyellow", fg="#00B000")
time_label.pack()

def tick():
    """Обновление табло электронных часов"""
    t = time.localtime(time.time())
    if t[5] % 2:  # эффект мигающего двоеточия
         fmt = "%H:%M"
    else:
         fmt = "%H %M"
    time_var.set(time.strftime(fmt, t))
    time_label.after(500, tick)  # следующий tick через 0.5 с

time_label.after(500, tick)
root.mainloop()