# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement 

# pseudocode
# ask user to input three numbers

import tkinter as tk

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))

# find the biggest number among the three using if-else (algorithm)
def find_biggest_number(number_1, number_2, number_3):
    if number_1 >= number_2 >= number_3:
        largest = number_1
    elif number_1 >= number_3 >= number_2:
        largest = number_1
    elif number_2 >= number_1 >= number_3:
        largest = number_2
    elif number_2 >= number_3 >= number_1:
        largest = number_2
    elif number_3 >= number_1 >= number_2:
        largest = number_3
    else:
        largest = number_3

    return largest

# get user input for three numbers
def calculate_biggest():
     try:
        first_number = get_inputted_number("Enter the first number:")
        second_number = get_inputted_number("Enter the second number:")
        third_number = get_inputted_number("Enter the third number:")
    except ValueError as e:
        # Display an error message for invalid input
        messagebox.showerror("Error", str(e))
        return

# create the first window
app = tk.Tk()
app.title("Finding the Biggest Number")

# create a button to start the program
start_button = tk.Button(app, text="Let's Start!", command=calculate_biggest)
start_button.pack(pady=20)

# print the result
print(f"The Biggest Number is: {biggest}")