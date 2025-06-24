"""A function is like a mini-program inside your program.
It helps us group steps together and reuse them anytime we want."""

"""
There are two parts of the function:
(I) Define a function: We create the function here using the def keyword, followed by function_name
(II) Calling a function: Write the function name followed by parentheses "()". """

#Task 1: Update the function calculator that prints substraction, multiplication of two numbers.

#Basic Function Example:
def greet():  #def is the keyword used to define a function.
    print("Hello!")
    print("Welcome to the coding class!")

greet()  # calling the function

#Function with a Parameter
def greet(name):
    print("Hello", name + "!")
    print("Hope you're having a great day!")

greet("Aarav")
greet("Meera")

#Update the below function to print the subtraction and multiplication of two numbers.
def calculator(a, b):
    return("Addition:", a + b)

print(calculator(6, 2))
