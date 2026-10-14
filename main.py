
import random
from collections import Counter

def number_game():
    number = random.randint(1, 10)
    attempts = 0

    print("\nGuess a number between 1 and 10!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess == number:
                score = max(10 - attempts + 1, 1)
                print("Correct! Attempts:", attempts)
                print("Your score:", score)
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")

def word_counter():
    filename = input("Enter text filename (e.g. sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.lower().split()
        counts = Counter(words)

        print("Total words:", len(words))
        print("Word frequency:")
        for word, count in counts.most_common():
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found. Please check the filename.")

while True:
    print("\n=== MENU ===")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        number_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
