# Write a program that
#  Saves a secret number in a variable.
#  Asks the user for a number guess.
#  Prints a bool False or True depending on whether the guess
# matches the secret.

secret = 5

guess = int(input("Guess a secret number: "))

print(f" Your guess is {guess == secret}")
