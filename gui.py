import main
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("790x720")

frame1 = Frame(root)
frame1.place(x=40, y=10)
frame2 = Frame(root)
frame2.place(x=10, y=10)

treev = ttk.Treeview(frame1, height=25)
treev.pack()

verscrlbar = ttk.Scrollbar(frame2, orient="vertical", command=treev.yview)
verscrlbar.pack()

# rowid first last number

# Defining the number of columns
treev["columns"] = ("1", "2", "3", "4")

# Defining the headings
treev['show'] = 'headings'

# Assigning the width and anchor to the respective columns

treev.column("1", width= 100, anchor='c')
treev.column("2", width= 200, anchor='c')
treev.column("3", width= 200, anchor='c')
treev.column("4", width= 200, anchor='c')


# Assigning the heading names to the respective columns
treev.heading("1", text="ROW ID")
treev.heading("2", text="First Name")
treev.heading("3", text="Last Name")
treev.heading("4", text="Phone Number")


def add_one(first, last, number):
    main.add_one(first, last, number)
    show()


def update(id, first, last, number):
    main.update(id, first, last, number)
    show()

def delete(id):
    main.delete(id)
    show()




id_label = Label(root, text="ROW ID: ")
id_label.place(x=10, y=550)
id_entry= Entry(root, width=10)
id_entry.place(x=70, y=550)

first_label = Label(root, text="FIRST NAME: ")
first_label.place(x=140, y=550)
first_entry= Entry(root,)
first_entry.place(x=218, y=550)

last_label = Label(root, text="LAST NAME: ")
last_label.place(x=340, y=550)
last_entry= Entry(root,)
last_entry.place(x=410, y=550)

number_label = Label(root, text="Phone: ")
number_label.place(x=540, y=550)
number_entry= Entry(root,)
number_entry.place(x=580, y=550)


create_button = Button(text="CREATE", bg="lightgreen", command=lambda:add_one(first_entry.get(), last_entry.get(), number_entry.get()))
create_button.place(x=720, y=550)

update_button = Button(text="UPDATE", bg="#f38630", command = lambda:update(id_entry.get(), first_entry.get(), last_entry.get(), number_entry.get()))
update_button.place(x=720, y=585)

delete_button = Button(text="DELETE", bg="#BC544B", command=lambda:delete(id_entry.get()))
delete_button.place(x=720, y=625)

def show():
    global treev
    treev.delete(*treev.get_children())
    for i in main.show_all():
        treev.insert("" , 'end', values = (i[0], i[1], i[2], i[3]))

show()
root.mainloop()