import random

secret_number = random.randint(1, 100)
max_attempts = 10

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number correctly.")
        break

    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print("Too High! Try again.")

else:
    print("Game Over!")
    print("The correct number was:", secret_number)
