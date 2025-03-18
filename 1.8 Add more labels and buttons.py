# Session 3
# Task 1: Make the date_label visible.
# Task 2: Add another button by name button2 with text as 'Upload Photo' similar to button2.
# Task 3: Add a submit button with the following properties:
# bg="black", fg="white",activebackground="blue",activeforeground="white"

import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24),
bg="blue", fg="white")
label1.pack(padx=10,pady=10)

#label to add text "Select Date"
date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white")
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

#button to upload a photo


#button to submit


root.mainloop()
