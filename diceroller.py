import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    print(f"You rolled a {roll_dice()}")
    play_again = input("Roll again? (y/n): ")
    if play_again.lower() != 'y':
        break
