# NEWTON-RAPHSON ROOT FINDER

user_input = float(input("Type a number: "))

epsilon = 0.01

guess = user_input/2.0

num_guesses = 0

while abs(guess * guess - user_input) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess ** 2) - user_input) / (2 * guess))
print(f"Number of guesses: {num_guesses}")
print(f"Square root of {user_input} is about {guess}")
