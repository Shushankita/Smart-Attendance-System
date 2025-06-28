#This imports the Tkinter module using the alias tk.
#Tkinter is a Python library used to create graphical user interfaces (GUIs).
#tk.Tk() creates the main window for the application.
#This window will serve as the root container for all other widgets (buttons, labels, etc.).
#The variable root holds the reference to this main window.
#root.mainloop Starts the Tkinter event loop, which keeps the window open.
#It waits for user interactions like button clicks, window closing, etc.
# Without a mainloop(), the window would appear and then immediately close.

""" Run and observe the code.
Task1: Change the title of the window to Smart Attendance System
Task2: Change the geometry to 500X300 """

import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Training Program")
root.geometry("500x500")

# Run the Tkinter event loop
root.mainloop()
