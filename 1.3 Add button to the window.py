'''Observe the code and find out the reason why the button is not visible.
Task1: Uncomment line20 to make the button visible.
Task2: Change the text on the button to "Select Excel File" '''
import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")
root.config(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white") 
label1.pack()

 #defining the width and height of the button in terms of pixels
button1 = tk.Button(root, text="Button1",width=20,height=2,bg="#B4A3D8")


#adding a border around the button and increasing its thickness
#button1.pack()

root.mainloop()
