# Swap values of two numbers

# Input the numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print the swapped numbers
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)