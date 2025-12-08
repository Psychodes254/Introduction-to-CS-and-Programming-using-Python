# APPROXIMATION METHOD TO
# FIND A “close enough” SQUARE ROOT

user_input = int(input("Type a number: "))
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess ** 2 - user_input) >= epsilon and guess ** 2 <= user_input:
    guess += increment
    num_guesses += 1
print(f"Number of guesses: {num_guesses}")
if abs(guess ** 2 - user_input) >= epsilon:
    print(f"There is no closer root for {user_input}")
else:
    print(f"{guess} is closer enough to {user_input}")