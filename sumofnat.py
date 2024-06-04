# Find sum of n natural numbers in Python with for loop

def calculate_sum(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    return sum

# Example usage
num = int(input("Enter a number: "))

total_sum = calculate_sum(num)
print(f"The sum of the first {num} natural numbers is: {total_sum}")