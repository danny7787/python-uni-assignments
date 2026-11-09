import random

# Choose a random number between 1 and 50.
secret_number = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50.")
print("You have 5 attempts.")

# Keep asking until the user has made 5 valid guesses.
while attempts < 5:
    user_input = input("Enter your guess: ")

    # Check that the input can be converted into a whole number.
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a whole number.")
        continue

    # Check that the number is within the allowed range.
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50.")
        continue

    # Count the guess after checking that it is valid.
    attempts += 1

    # Compare the guess with the secret number.
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print("Too low, try again.")

    # Show how many attempts remain or end the game.
    if attempts == 5:
        print("You have used all 5 attempts.")
        print("The number was:", secret_number)
    else:
        print("Attempts left:", 5 - attempts)

