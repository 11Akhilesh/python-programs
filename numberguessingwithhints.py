import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
