def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
