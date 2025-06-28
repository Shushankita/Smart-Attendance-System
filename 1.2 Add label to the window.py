#tk.Label creates a text display area on the window on line 24.
#text="Label1" sets the label's displayed text.
#font=("Courier New", 24) sets the font style and font size.
#bg="black" sets the background color of the label.
#fg="white" sets the text (foreground) color.
#.pack() places the label on the window (centred by default).

'''Task 1: Change the text on the label to Smart Attendance System
Task 2: Select any other font style from lines 31 to 39. Remove all the other font styles from the code.
Task 3: The students must change the value of bg in line 20 to blue. '''

import tkinter as tk  # Import the tkinter module and use alias tk

# Create the main tkinter window
root = tk.Tk()
root.title("Training Program")           # Set the title of the window
root.geometry("500x300")                 # Set the window size to 500x300 pixels

# Task 3: Set the background colour to blue
root.config(bg='blue')                  # Background color of the main window

# Task 1 & Task 2:
# Create a label with updated text and font style (font style changed to Arial, size 24)
label1 = tk.Label(
    root,
    text="Smart Attendance System",      # Updated label text (Task 1)
    font=("Arial", 24),                  # Font style changed (Task 2)
    bg="black",                          # Background color of label
    fg="white"                           # Foreground/text color of label
)
"""List of font-style available
1. Arial
2. Times New Roman
3. Comic Sans MS
4. Courier New
5. Impact
6. Georgia
7. Lexend (
8. Comfortaa"""
label1.pack()  # Display the label on the window

# Run the Tkinter event loop to keep the window open
root.mainloop()
