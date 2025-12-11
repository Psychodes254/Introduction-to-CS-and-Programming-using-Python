# Assume you are given an integer 0 <= N <= 1000. 
# Write a piece of Python code that uses bisection search to guess N. 
# The code prints two lines: count: with how many guesses it tooN to find N, 
# and N: with the value of N. 
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

user_input = int(input("Type a number between 0 and 1000: "))

high = 1001

low = 0

count = 0


while low < high:
    
    guess = (low + high) // 2
    
    count += 1
    
    if guess < user_input:
        low = guess +1
    else:
        high = guess
    
print(f"Number of guesses: {count}")