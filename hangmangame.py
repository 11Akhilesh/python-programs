import random

words = ["python", "java", "swift", "javascript"]
word = random.choice(words)
guessed_letters = []
attempts = 6
display_word = ["_"] * len(word)

print("Welcome to Hangman!")

while attempts > 0 and "_" in display_word:
    print("Word: " + " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display_word[i] = guess
        guessed_letters.append(guess)
    else:
        attempts -= 1
        guessed_letters.append(guess)
        print(f"Wrong guess. Attempts left: {attempts}")

if "_" not in display_word:
    print("Congratulations! You guessed the word: " + word)
else:
    print(f"Game over. The word was: {word}")
