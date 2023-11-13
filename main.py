import tkinter as tk
from tkinter import *
import pyshorteners as pys

gui = Tk()
gui.title("URL Shortener")
gui.geometry("800x400")


def shorturl():
    URL_entry = URL.get()
    result = pys.Shortener().tinyurl.short(URL_entry)
    URLentry.insert(END, result)
    message_label.config(text="URL is shortened!")
    
Label(gui,
      text="URL Shortener",
      font=("Arial 20 bold"),
      fg="Red").pack(pady=10)

frame1 = Frame(gui)
Label(frame1,
        text = "Paste URL Here:",
        font = ("Aria 12")).pack(pady=10)

URL = Entry(frame1,
            width=35,
            font = ("Aria 12"))

URL.pack()
URL.focus_set()
frame1.pack(pady=10)

Button(gui,
       text = "Generate Link",
       font = ("Arial 10"),
       command=shorturl).pack(pady=5)

frame2 = Frame(gui)
Label(frame2,
      text = "Copy URL: ",
      font = ("Arial 12")).pack(pady=10)

URLentry = Entry(frame2,
                 width="25",
                 fg = "blue",
                 font = ("Arial 12"))
URLentry.pack()
frame2.pack(pady=10)

message_label = Label(gui, text="", font=("Arial 12"), fg="green")
message_label.pack(pady=10)


gui.mainloop()