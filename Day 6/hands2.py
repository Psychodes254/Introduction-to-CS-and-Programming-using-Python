# BISECTION SEARCH – SQUARE
# ROOT for ALL x VALUES

user_input = float(input("Type a number: "))
epsilon = 0.1

if user_input <= 0:
    low = user_input
    high = 1.0
else:
    low = 1.0
    high = user_input

guess = (high + low) / 2

while abs(guess ** 2 - user_input) >= epsilon:
    if guess ** 2 > user_input:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
print(f"The closest root is {guess}")
