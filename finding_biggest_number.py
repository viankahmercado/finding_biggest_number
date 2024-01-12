# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement 

import tkinter as tk
from tkinter import simpledialog, messagebox

def get_inputted_number(prompt):
    while True:
        try:
            # Use simpledialog to get inputted number
            user_input = simpledialog.askfloat("Input", prompt)
            if user_input is not None:
                return user_input
            else:
                raise ValueError("Please enter a valid number.")
        except ValueError as e:
            # Show an error message if the input is not a valid number
            messagebox.showerror("Error", str(e))

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
    
    # Find the biggest number using the defined function
    largest_number = find_biggest_number(first_number, second_number, third_number)

    # Display the result using a message box
    messagebox.showinfo("Result", f"The Biggest Number is: {largest_number}")

# create the main application window
app = tk.Tk()
app.title("Finding the Biggest Number")
app.geometry("400x400")

# create a button to start the program
label_description = tk.Label(text="BIGGEST NUMBER SIMULATOR", font=('Helvetica',15), bd=4, relief="sunken")
label_description.place(relx=0.5, rely=0.3, anchor="center")

start_button = tk.Button(app, text="Let's Start!", command=calculate_biggest, font=('Helvetica',15), bd=4, bg='#FF5733', fg='white')
start_button.place(relx=0.5, rely=0.5, anchor="center")

# run the Tkinter event loop
app.mainloop()