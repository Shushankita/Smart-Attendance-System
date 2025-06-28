# On line 44 to 45 text_widget = tk.Text(root)
# This line creates a Text widget, which is used in Tkinter to:
# Display or accept multi-line text input.
# Unlike Entry, which is single-line, Text allows paragraphs, scrolling, and formatting.
# root is the parent window where the widget will appear.

import tkinter as tk
from tkcalendar import DateEntry

def update(*args):
  date_label.config(text="Selected date is " + date_var.get())

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
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white")
button2.config(highlightbackground = "black",highlightthickness=3)
button2.pack(pady=10)

# Create a Text widget for displaying extracted text
text_widget = tk.Text(root)
text_widget.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",
fg="white",activebackground="blue",activeforeground="white")
submit.pack(pady=10)

root.mainloop()
