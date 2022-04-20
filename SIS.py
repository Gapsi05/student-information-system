import csv
import tkinter as tk
from tkinter import Button, ttk
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("STUDENT INFORMATION SYSTEM")

# Background Color
win.config(bg="#F3CF04")

# Adding some style
style = ttk.Style()

# Pick a theme
style.theme_use("default")

style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=27,
                fieldbackground="white"
                )

# Change selected color
style.map(
    "Treeview",
    background=[("selected", "#030E3E")]
)

# Top Menu
title_label = tk.Label(
    win,
    text="STUDENT INFORMATION SYSTEM",
    font=("Hops And Barley c3 Bold", 30, "bold"),
    padx=15,
    pady=15,
    border=0,
    relief=tk.GROOVE,
    bg="#030E3E",
    foreground="#F3CF04"
)
title_label.pack(side=tk.TOP, fill=tk.X)

# Left Menu
detail_frame = tk.LabelFrame(
    win, text="-_-_-STUDENT RECORDS-_-_-",
    font=("Hops And Barley c3 Bold", 20),
    bg="#F3CF04",
    foreground="#030E3E",
    relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=340)

menu_frame = tk.LabelFrame(
    win, text="-_-_-_-_-_-MENU-_-_-_-_-_-",
    font=("Hops And Barley c3 Bold", 20),
    bg="#F3CF04",
    foreground="#030E3E",
    relief=tk.GROOVE
)

menu_frame.place(x=40, y=450, width=420, height=217)

# Name
name_lab = tk.Label(
    detail_frame,
    text="  Name:   ",
    font=("Hops And Barley c3 Bold", 17),
    bg="#030E3E",
    foreground="#F3CF04"
)
name_lab.place(x=20, y=16.5)

name_ent = tk.Entry(
    detail_frame,
    bd=5,
    font=("Calibre", 13),
    bg="white",
    foreground="black"
)
name_ent.place(x=125, y=17, width=250, height=30)

# ID No.
id_lab = tk.Label(
    detail_frame,
    text="  ID No.:    ",
    font=("Hops And Barley c3 Bold", 17),
    bg="#030E3E",
    foreground="#F3CF04"
)
id_lab.place(x=20, y=65)

id_ent = tk.Entry(
    detail_frame,
    bd=5,
    font=("Calibre", 13),
    bg="white",
    foreground="black"
)
id_ent.place(x=125, y=65, width=250, height=30)

# Year level
year_lab = tk.Label(
    detail_frame,
    text="  Year:   ",
    font=("Hops And Barley c3 Bold", 17),
    bg="#030E3E",
    foreground="#F3CF04"
)
year_lab.place(x=20, y=113)

year_ent = ttk.Combobox(
    detail_frame,
    font=("Calibre", 13),
)
year_ent["values"] = ("1ST YEAR", "2ND YEAR", "3RD YEAR", "4TH YEAR", "5TH YEAR")
year_ent.place(x=125, y=113, width=250, height=30)

# Gender
gen_lab = tk.Label(
    detail_frame,
    text="Gender:   ",
    font=("Hops And Barley c3 Bold", 17),
    bg="#030E3E",
    foreground="#F3CF04"
)
gen_lab.place(x=20, y=161)

gen_ent = ttk.Combobox(
    detail_frame,
    font=("Calibre", 13),
)
gen_ent["values"] = ("MALE", "FEMALE")
gen_ent.place(x=125, y=161, width=250, height=30)

# Course
course_lab = tk.Label(
    detail_frame,
    text="Course: ",
    font=("Hops And Barley c3 Bold", 17),
    bg="#030E3E",
    foreground="#F3CF04"
)
course_lab.place(x=20, y=209)

course_ent = tk.Entry(
    detail_frame,
    bd=5,
    font=("Calibre", 13),
    bg="white",
    foreground="black"
)
course_ent.place(x=125, y=209, width=250, height=30)

# Search
search_lab = tk.Label(
    menu_frame,
    text="SEARCH:   ",
    font=("Hops And Barley c3 Bold", 17),
    bg="#030E3E",
    foreground="#F3CF04"
)
search_lab.place(x=20, y=135)

search_ent = tk.Entry(
    menu_frame,
    bd=5,
    font=("Calibre", 16),
    bg="white",
    foreground="black",
)

search_ent.place(x=125, y=135, width=268, height=30)

text = tk.Label(
    menu_frame,
    text="(Please input the ID Number)",
    font=("Arial", 7),
    bg="#F3CF04",
    foreground="#030E3E"
)
text.place(x=125, y=165)

# Database frame
data_frame = tk.Frame(
    win,
    bg="#F3CF04",
    relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=830, height=565)

main_frame = tk.Frame(
    data_frame,
    bg="#030E3E",
    bd=7,
    relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# Treeview database
student_table = ttk.Treeview(main_frame, columns=(
    "ID Number", "Name", "Course", "Year", "Gender",
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID Number", text="ID Number")
student_table.heading("Name", text="Name")
student_table.heading("Course", text="Course")
student_table.heading("Year", text="Year")
student_table.heading("Gender", text="Gender")

student_table["show"] = "headings"

student_table.column("ID Number", width=25)
student_table.column("Name", width=200)
student_table.column("Course", width=175)
student_table.column("Year", width=25)
student_table.column("Gender", width=25)

student_table.pack(fill=tk.BOTH, expand=True)

# Students Data
with open('data.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        idNo = row['id#']
        name = row['name']
        course = row['course']
        year = row['year']
        gender = row['gender']
        student_table.insert("", 0, values=(idNo, name, course, year, gender))

# Functions
global count
count = 0
data = []
for record in data:
    if count % 2 == 0:
        student_table.insert(parent="", index="end", iid=count, text="", values=())
    else:
        student_table.insert(parent="", index="end", iid=count, text="", values=())

    count += 1

# Add Function
def add_record():
    global count
    if count % 2 == 0:
        student_table.insert(parent="", index="end", iid=count, text="", values=(
            id_ent.get(),
            name_ent.get(),
            course_ent.get(),
            year_ent.get(),
            gen_ent.get(),
        ),
                             )
    else:
        student_table.insert(parent="", index="end", iid=count, text="", values=(
            id_ent.get(),
            name_ent.get(),
            course_ent.get(),
            year_ent.get(),
            gen_ent.get(),
        ),
                             )
    count += 1

# Delete One Function
def delete_one():
    x = student_table.selection()[0]
    student_table.delete(x)

# Edit Function
def edit_record():
    id_ent.delete(0, END)
    name_ent.delete(0, END)
    course_ent.delete(0, END)
    year_ent.delete(0, END)
    gen_ent.delete(0, END)

    selected = student_table.focus()
    values = student_table.item(selected, "values")

    id_ent.insert(0, values[0])
    name_ent.insert(0, values[1])
    course_ent.insert(0, values[2])
    year_ent.insert(0, values[3])
    gen_ent.insert(0, values[4])

# Update Function
def update_record():
    selected = student_table.focus()
    student_table.item(selected, text="",
                       values=(id_ent.get(), name_ent.get(), course_ent.get(), year_ent.get(), gen_ent.get()))

    id_ent.update(0, END)
    name_ent.update(0, END)
    course_ent.update(0, END)
    year_ent.update(0, END)
    gen_ent.update(0, END)

# Clear Function
def delete_all():
    id_ent.delete(0, END)
    name_ent.delete(0, END)
    course_ent.delete(0, END)
    year_ent.delete(0, END)
    gen_ent.delete(0, END)

# Buttons
btn_frame = tk.Frame(
    detail_frame,
    bg="#F3CF04",
    bd=0,
    relief=tk.GROOVE
)
btn_frame.place(x=20, y=400, width=370, height=100)

btn_frame_clear = tk.Frame(
    detail_frame,
    bg="#F3CF04",
    bd=0,
    relief=tk.GROOVE
)
btn_frame_clear.place(x=60, y=250, width=310, height=50)

# Add Button
add_btn = tk.Button(
    menu_frame,
    bg="#030E3E",
    foreground="#F3CF04",
    text="ADD",
    bd=1,
    font=("Hops And Barley c3 Bold", 15), width=12,
    command=add_record
)
add_btn.grid(row=1, column=0, padx=20, pady=15)

# Edit Button
edit_btn = tk.Button(
    menu_frame,
    bg="#030E3E",
    foreground="#F3CF04",
    text="EDIT",
    bd=1,
    font=("Hops And Barley c3 Bold", 15), width=12,
    command=edit_record
)
edit_btn.grid(row=1, column=1, padx=25, pady=15)

# Delete Button
delete_btn = tk.Button(
    menu_frame,
    bg="#030E3E",
    foreground="#F3CF04",
    text="DELETE",
    bd=1,
    font=("Hops And Barley c3 Bold", 15), width=12,
    command=delete_one
)
delete_btn.grid(row=2, column=0, padx=20, pady=2)

# Update Button
update_btn = tk.Button(
    menu_frame,
    bg="#030E3E",
    foreground="#F3CF04",
    text="UPDATE",
    bd=1,
    font=("Hops And Barley c3 Bold", 15), width=12,
    command=update_record
)
update_btn.grid(row=2, column=1, padx=25, pady=15)

# Clear Button
clear_btn = tk.Button(
    btn_frame_clear,
    bg="#030E3E",
    foreground="#F3CF04",
    text="CLEAR",
    bd=1,
    font=("Hops And Barley c3 Bold", 15), width=7,
    command=delete_all
)
clear_btn.grid(row=1, column=1, padx=208, pady=15)

win.mainloop()
