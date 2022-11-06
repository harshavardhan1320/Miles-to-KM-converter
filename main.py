from tkinter import *

window = Tk()
window.title("MY WINDOW")
window.minsize(400, 500)

my_label = Label(text="I'M A LABEL", font=("Arial", 14))
my_label.pack()

my_label["text"] = "new_label"
my_label.config(text="new_label")

# Button


def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.pack()

# Entry

entry = Entry(width=25)
# add some text to begin with
entry.insert(END, string="Some text to begin with.")
# gets text in entry
print(entry.get())
entry.pack()

# Text

text = Text(height=5, width=30)
# puts curser in textbox
text.focus()
text.insert(END, "example of multiline text entry")
# gets current value in the textbox at line 1,character 0
print(text.get("1.0", END))
text.pack()

# Scale

# calling with the current scale value


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# spinbox


def spinbox_used():
    # gets the current value in the spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# checkbutton


def checkbutton_used():
    print(check_state.get())


# variable is to hold the checked state, 0 is off and 1 is on
check_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=check_state, command=checkbutton_used)
check_state.get()
checkbutton.pack()

# Radio button


def radio_used():
    print(radio_state.get())


# variable to hold on the which redio button is clicked
radio_state = IntVar()
radio_button1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

# Listbox


def listbox_used():
    # get the curser selected from the listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["banana", "apple", "pear", "mellon"]
for items in fruits:
    listbox.insert(fruits.index(items), items)
listbox.bind("<<listbox select>>", listbox_used)
listbox.pack()




window.mainloop()
