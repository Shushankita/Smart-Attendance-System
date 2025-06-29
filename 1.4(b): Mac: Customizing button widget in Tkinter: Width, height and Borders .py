#bd (border width) defines how thick the border looks.
#relief controls the style of the border (e.g., solid, flat, raised).
#Together, these lines give the button a clear edge/border effect.

#Task 1: change the bd value from 5 to 3 and observe the difference.

import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")
root.config(bg='skyblue')

label1 = tk.Label(
    root,
    text="Smart Attendance System",
    font=("Courier New", 24),
    bg="blue",
    fg="white"
)
label1.pack()

button1 = tk.Button(
    root,
    text="Select Excel File",   # Text displayed on the button
    width=20,                   # Width of the button (in character units)
    height=2,                   # Height of the button (in text lines)
    bg="#B4A3D8"                # Background color of the button
)

# Customize the button appearance
button1.config(highlightbackground = "blue",highlightthickness=3)#adding border around the button and increasing it's thickness
button1.pack()

root.mainloop()
