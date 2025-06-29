#padx=10: Adds 10 pixels of space to the left and right of the widget.
#pady=10: Adds 10 pixels of space to the top and bottom of the widget.
#This helps in visually separating widgets from the edges of the window or from each other.
#state=tk.DISABLED prevents user interaction with the button.

# Task 1: Change the padding from 5 to 10 on lines 35 and 25.
# Task 2: Change button state from DISABLEd to NORMAL/ACTIVE on line 31.

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
label1.pack(padx=5, pady=5)         # Apply horizontal and vertical padding (Task 1)

button1 = tk.Button(root,
    text="Select Excel File",
    width=20,
    height=2,
    bg="#B4A3D8",
    activebackground="grey",
    activeforeground="white",
    state=tk.DISABLED
)  # <-- closing parenthesis added here
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack()

root.mainloop()
