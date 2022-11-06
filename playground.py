from tkinter import *

window = Tk()
window.title("MY WINDOW")
window.minsize(200, 200)
window.config(padx=40, pady=40)

my_label = Label(text="I'M A LABEL", font=("Arial", 14))
my_label.grid(column=0, row=0)

my_label["text"] = "new_label"
my_label.config(text="new_label")

# Button


def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)


button1 = Button(text="Button", command=button_clicked)
button2 = Button(text="New button", command=button_clicked)

button1.grid(column=2, row=1)
button2.grid(column=3, row=0)

# Entry

entry = Entry(width=25)
# add some text to begin with
entry.insert(END, string="Some text to begin with.")
# gets text in entry
print(entry.get())
entry.grid(column=4, row=4)



window.mainloop()
