# Write a program that
#  Saves a secret number.
#  Asks the user for a number guess.
#  Prints whether the guess is too low, too high, or the same as the secret.

secret = 10 

guess = int(input("Guess a number: "))

if guess > secret:
    print("Your guess is too high!")
elif guess < secret:
    print("Your guess is too low!")
else:
    print("Your guess is the same as the secret number!")
