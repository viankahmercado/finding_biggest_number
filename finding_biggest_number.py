# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement 

# pseudocode
# ask user to input three numbers

import tkinter as tk

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))

# find the biggest number among the three (algorithm)
if number_1 >= number_2 >= number_3:
    biggest = number_1
elif number_1 >= number_3 >= number_2:
    biggest = number_1
elif number_2 >= number_1 >= number_3:
    biggest = number_2
elif number_2 >= number_3 >= number_1:
    biggest = number_2
elif number_3 >= number_1 >= number_2:
    biggest = number_3
else:
    biggest = number_3

# create the first window
app = tk.Tk()
app.title("Finding the Biggest Number")

# create a button to start the program
start_button = tk.Button(app, text="Let's Start!", command=calculate_biggest)
start_button.pack(pady=20)

# print the result
print(f"The Biggest Number is: {biggest}")