from tkinter import *

def kwadraat():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

def wortel():
    grondtal = int(entry.get())
    wortel = grondtal ** (1/2)
    tekst = "Wortel: van {} = {}"
    label["text"] = tekst.format(grondtal, wortel)

root = Tk()

label = Label(master=root, text='Hello world', height=2)
label.pack()

button = Button(master=root, text='Druk voor kwadraat', command=kwadraat)
button.pack(pady=10, padx=10, fill=X)

button2 = Button(master=root, text='Druk voor wortel', command=wortel)
button2.pack(pady=10, padx=10, fill=X)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()
