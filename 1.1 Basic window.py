"""Task1: Change the title of the code to Smart Attendance System
Task2: Change the text on the button to 'Select the Excel sheet' """

import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

# Create a label widget
label1 = tk.Label(root, text="Smart Attendance System")
label1.pack()

# Create a button to select the Excel file
button1 = tk.Button(root, text="Button1")
button1.pack()

# Run the tkinter event loop
root.mainloop()
