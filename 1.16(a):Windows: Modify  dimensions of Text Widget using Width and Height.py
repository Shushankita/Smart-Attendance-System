# On line 47 width=50
# Sets the width of the Text widget to approximately 50 characters.
# That means the widget can show up to 50 characters horizontally before
# wrapping text (if wrapping is enabled).
# On line 48 height=10
# Sets the height to 10 lines of text.
# That means the widget can display 10 rows of text vertically without scrolling.

#Task : Change the width and height on line 47 and observe the change.

import tkinter as tk
from tkcalendar import DateEntry

def update(*args):
  date_label.config(text="Selected date is "+date_var.get())

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)

date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,
justify="center",state="normal",selectbackground="blue",textvariable=date_var)
date_entry.pack(pady=5)

date_var.trace('w', update)

button1 = tk.Button(root, text="Select Excel File",width=20,
height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white")
button1.config(bd = 5,relief="solid")
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white")
button2.config(bd = 5,relief="solid")
button2.pack(pady=10)

text_widget = tk.Text(root,width=50,height=10) #adding width and height of the text field
text_widget.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,
bg="black",fg="white",activebackground="blue",activeforeground="white")
submit.pack(pady=10)

root.mainloop()
