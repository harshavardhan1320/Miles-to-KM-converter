from tkinter import *

window = Tk()
window.minsize(width=100, height=100)
window.config(pady=30, padx=30)

entry = Entry(width=5)
entry.insert(END, string="0")
entry.grid(column=1, row=0)


km = Label(text=0)
KM = Label(text="Km")
mile = Label(text="Miles")
eql = Label(text="is equals to")
km.grid(column=1, row=1)
KM.grid(column=2, row=1)
mile.grid(column=2, row=0)
eql.grid(column=0, row=1)



def button_clicked():
    miles = int(entry.get())
    kilometer = round(miles * 1.609, 2)
    km.config(text=kilometer)


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)

window.mainloop()
