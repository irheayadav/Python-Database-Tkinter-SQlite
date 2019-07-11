##GUI +Database


from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Database")

import sqlite3 #split library ##database

connection = sqlite3.connect('student1_detail.db')
print("database opened successfully")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY "
                    " AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
print("table created sucessfully. ")


label_1 = tk.Label(root, text="Student Name")
label_1.pack()
name_field1 = tk.Entry(root)
name_field1.pack()


label_2 = tk.Label(root, text="Student College")
label_2.pack()
name_field2 = tk.Entry(root)
name_field2.pack()


label_3 = tk.Label(root, text="Student Address")
label_3.pack()
name_field3 = tk.Entry(root)
name_field3.pack()

label_4 = tk.Label(root, text="Student Phone")
label_4.pack()
name_field4 = tk.Entry(root)
name_field4.pack()

def database():
    name = name_field1.get()
    college = name_field2.get()
    address = name_field3.get()
    phone = name_field4.get()
    # print(name1, name2, name3, name4)

    connection.execute(" INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + " , " + STUDENT_COLLEGE + " , "
                       + STUDENT_ADDRESS + " , " + STUDENT_PHONE + " ) VALUES ( '"+name +"',' " +
                       college+ "',  " + " '"+address+"', "+phone+ ");")
    connection.commit()
    messagebox.showinfo("Your data has been sucessfully saved")

butt1 = tk.Button(root, text="Save", command=lambda: database())
butt1.pack()



def retrive():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("Student id is: ", row[0])
        print("Student name is: ", row[1])
        print("Student college is: ", row[2])
        print("student Address is:", row[3])
        print("Student phone is:", row[4])


butt2 = tk.Button(root, text="Retrive", command=lambda: retrive())
butt2.pack()

root.mainloop()



















