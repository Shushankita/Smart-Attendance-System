'''Task1: Change the text on the label to Smart Attendance System
Task2: Select any other font style from lines 16 to 23. Remove all the other font styles from the code.
Task 3: The students must change the value of bg in line 15 to blue. '''

import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

# Set the background colour to blue
root.config(bg='skyblue')


label1 = tk.Label(root, text="Label1", font=("Courier New", 24), bg="black", fg="white") #changing the font style and adding foreground color(fg) and background color(bg)
"""List of font-style available
1. Arial
2. Times New Roman
3. Comic Sans MS
4. Courier New
5. Impact
6. Georgia
7. Lexend (
8. Comfortaa"""
label1.pack()


root.mainloop()
