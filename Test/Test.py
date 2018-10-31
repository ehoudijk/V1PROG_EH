from tkinter import *
import xmltodict


window = Tk()
window.geometry('700x400')
window.configure(background="#FFFFFF")

FrameOverOns = Frame(master=window)
FrameOverOns.configure(background="#FFFFFF")

FrameReizen = Frame(master=window)
FrameReizen.configure(background="#FFFFFF")

FrameHandleiding = Frame(master=window)
FrameHandleiding.configure(background="#FFFFFF")

HandleidingLabel = Label(master=FrameHandleiding, text="hallo", background="#FFFFFF")
HandleidingLabel.pack()


def processXML(openfile):
    with open(openfile) as openXMLFile:
        filecontent = openXMLFile.read()
        xmldictionary = xmltodict.parse(filecontent)
        return xmldictionary

berichten = processXML("teksten.xml")
berichten = berichten['berichten']


def redirect(van, naar):
    van.pack_forget()
    naar.pack()


def terugknop1(master):
    TerugKnop = Button(master=master, command=lambda van=master, naar=mainframe: redirect(van, naar), text='Terug', font=("Helvetica", 10, "bold"), background="#63a3f2", width=5, height=3, relief="flat",)
    TerugKnop.bind("<Enter>", lambda event, b=TerugKnop: b.configure(background="#4292f4"))
    TerugKnop.bind("<Leave>", lambda event, b=TerugKnop: b.configure(background="#63a3f2"))
    TerugKnop.place(x=0, y=0)


def Reizen():
    mainframe.pack_forget()
    FrameReizen.pack(fill="both", expand=True)
    terugknop1(FrameReizen)


def OverOns():
    mainframe.pack_forget()
    FrameOverOns.pack(fill="both", expand=True)
    terugknop1(FrameOverOns)
    label = Label(FrameOverOns, text=berichten['textMain'], font=("Helvetica", 10), background="#FFFFFF").pack()


def Handleiding():
    mainframe.pack_forget()
    FrameHandleiding.pack(fill="both", expand=True)
    terugknop1(FrameHandleiding)

def Afsluiten():
    quit()


mainframe = Frame(master=window)
mainframe.configure(background="#FFFFFF")
mainframe.pack(fill="both", expand=True)

MainLabel = Label(master=mainframe, background='#FFFFFF', text='NS-APP', font=('Helvetica', 24, 'bold'), height=3)
MainLabel.pack(fill='x')

ButtonFrame = Frame(master=mainframe, background="#FFFFFF")
ButtonFrame.pack()

ButtonReizen = Button(master=ButtonFrame, command=Reizen,background="#63a3f2", text='Reizen',font=('helvetica', 12, 'bold'), width=20,height=4, relief="flat")
ButtonReizen.bind("<Enter>", lambda event, b=ButtonReizen: b.configure(background="#4292f4"))
ButtonReizen.bind("<Leave>", lambda event, b=ButtonReizen: b.configure(background="#63a3f2"))
ButtonReizen.grid(row=0, column=0, padx=5, pady=5)

ButtonInfo = Button(master=ButtonFrame, command=Handleiding, background="#63a3f2", text='Handleiding', font=('helvetica', 12, 'bold'), width=20, height=4, relief="flat")
ButtonInfo.bind("<Enter>", lambda event, b=ButtonInfo: b.configure(background="#4292f4"))
ButtonInfo.bind("<Leave>", lambda event, b=ButtonInfo: b.configure(background="#63a3f2"))
ButtonInfo.grid(row=0, column=1)

ButtonOverOns = Button(master=ButtonFrame, command=OverOns, background="#63a3f2", text='Over ons', font=('helvetica', 12, 'bold'), width=20, height=4, relief="flat" )
ButtonOverOns.bind("<Enter>", lambda event, b=ButtonOverOns: b.configure(background="#4292f4"))
ButtonOverOns.bind("<Leave>", lambda event, b=ButtonOverOns: b.configure(background="#63a3f2"))
ButtonOverOns.grid(row=1, column=0)

ButtonAfsluiten = Button(master=ButtonFrame,background="#63a3f2", command=Afsluiten, text='Afsluiten', font=('helvetica', 12, 'bold'), width=20, height=4, relief="flat")
ButtonAfsluiten.bind("<Enter>", lambda event, b=ButtonAfsluiten: b.configure(background="#4292f4"))
ButtonAfsluiten.bind("<Leave>", lambda event, b=ButtonAfsluiten: b.configure(background="#63a3f2"))
ButtonAfsluiten.grid(row=1, column=1)

window.mainloop()
