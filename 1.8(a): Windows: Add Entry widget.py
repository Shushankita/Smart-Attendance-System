# The Entry widget in Tkinter is used to accept single-line user input
# — such as a name, date, or number.
# entry = tk.Entry(root) creates an entry field (input box) in the specified window
# or frame (root in this case).


# Task: Modify the entry widget configuration as given below on line 38 & 39.

import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.config(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24),
bg="blue", fg="white")
label1.pack(padx=10,pady=10)

# Create a label for the date entry field
date_label = tk.Label(
    root,
    text="Select Date:",                # Label text displayed above the entry box
    font=("Courier New", 10),          # Font style and size
    bg="skyblue"                       # Background color matching the window
)
date_label.pack(pady=5)                # Add vertical spacing around the label

# Create an entry widget to accept user input (e.g., a date)
date_entry = tk.Entry(
    root,
    relief="sunken",                   # Border style: 'sunken' gives a pressed-in look
    borderwidth=3,                     # Thickness of the border
    justify="center"                   # Align the text in the center of the entry box
)
# Possible relief values: flat, sunken, raised, groove, ridge
# Justify options: left, center, right

date_entry.pack(pady=5)               # Add vertical spacing around the entry widget

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white")
button1.config(bd = 5,relief="solid")
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button2.config(bd = 5,relief="solid")
button2.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",
fg="white",activebackground="blue",activeforeground="white")
submit.pack(pady=10)

root.mainloop()
