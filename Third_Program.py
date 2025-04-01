# Taking input from the user
user_input = input("Enter something: ")

# Printing the input back to the user
try:
    x = int(user_input)
    print("You entered the integer:", x)
except ValueError:
    print("Invalid input. Please enter an integer.")