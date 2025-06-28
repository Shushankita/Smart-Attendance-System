#In this code, interactivity is added to the button using activebackground and activeforeground
#options.
#These settings change the button's appearance while it is being clicked by the user,
#making the UI feel more responsive and dynam

# Task: Change the button configuration when clicked to a different color.

import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.config(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white")
label1.pack()

#adding background and foreground color for the button when user clicks on it
button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white")

button1.config(bd = 5,relief="solid")
button1.pack()

root.mainloop()
