# tkcalendar is a third-party Python module that provides calendar and date picker 
# widgets for use with Tkinter GUI applications.
# It helps users to select a date from a calendar interface instead of manually typing it in an Entry box.
# DateEntry
# A drop-down calendar widget.
# Works like a Tkinter Entry, but clicking on it opens a small calendar to choose a date.
# Useful for form inputs like birthdates, attendance dates, deadlines, etc.


# Calendar
# A full calendar view where users can navigate and select a date.
# More visual and interactive than DateEntry.

# Task 1: pip install tkcalendar in the terminal window
# Task 2: Change the configuration of DateEntry widget

import tkinter as tk
from tkcalendar import DateEntry #importing DateEntry widget from the tkcalendar module

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.config(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24),
bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)
date_entry = DateEntry(root,relief="sunken",borderwidth=3,justify="center",
state="normal",selectbackground="black") #changing entry widget to DateEntry for date selection
date_entry.pack(pady=5)

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button1.config(bd = 5,relief="solid")
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button2.config(bd = 5,relief="solid")
button2.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",fg="white",
activebackground="blue",activeforeground="white")
submit.pack(pady=10)

root.mainloop()
