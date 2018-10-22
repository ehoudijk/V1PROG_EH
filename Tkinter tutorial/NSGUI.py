from tkinter import *
from NSCODE import *


def stations():
    vertrekstation = station_entry.get()
    res = aanvrager(vertrekstation)
    test = ''
    for i in range(5):
        test += res[i]

    label["text"] = test

root = Tk()

station_entry = Entry(master=root)
station_entry.pack(padx=10, pady=10)

button = Button(master=root, text='Voer uw vertrekstation in', command=stations)
button.pack(pady=10, padx=10, fill=X)

label = Label(master=root, text='Invoer', height=40)
label.pack()

root.mainloop()
