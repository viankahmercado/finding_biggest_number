# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement 

# pseudocode
# ask user to input three numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))

# find the biggest number among the three (algorithm)
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
    
# print the result
print(f"The largest number is: {largest}")