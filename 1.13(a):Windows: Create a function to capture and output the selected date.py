#Updating the date label to change the text. date_var.get() is used to
#get the selected date from the date entry widget on line 8.

# Task - Make the change on line no 11 to add a Space after is - Output should look like below.
# Selected date is 28/06/2025.

import tkinter as tk
from tkcalendar import DateEntry

def update():#defining function to display the selected date
  date_label.config(text="Selected date is"+date_var.get())

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24),
bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)

date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,
justify="center",state="normal",selectbackground="blue",textvariable=date_var)
date_entry.pack(pady=5)

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white")
button1.config(bd = 5,relief="solid")
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button2.config(bd = 5,relief="solid")
button2.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",
fg="white",activebackground="blue",activeforeground="white",command=update)
submit.pack(pady=10)

root.mainloop()
