# Task: Change the state of the button from DISABLED to NORMAL / ACTIVE 

import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.config(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", 
font=("Courier New", 24), bg="blue", fg="white") 
label1.pack()

button1 = tk.Button(root, text="Select Excel File",width=20,
height=2,bg="#B4A3D8",activebackground="grey",
activeforeground="white",state=tk.DISABLED)  #adding state of the button

#possible value for state: tk.NORMAL, tk.DISABLED, tk.ACTIVE

button1.config(bd = 5,relief="solid")
button1.pack()

root.mainloop()
