# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0
high = x
ans = (low + high) / 2

while abs((ans ** 4) - x) >= epsilon:
    if ans ** 4 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2

# print(f"Fourth root of {x} is approximate {ans}")


# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 
def check_num_in_range(num, start, finish):
    
    return start <= num and finish >= num

# print(check_num_in_range(3, 1, 5))
# print(check_num_in_range(3, 5, 7))


# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
def perfect_num(num):
    
    divisors = sum([x for x in range(1, num) if num % x == 0])
    
    return num == divisors
    
# print(perfect_num(6))
# print(perfect_num(28))
# print(perfect_num(50))


# Problem 4 - Approximation Algorithm
# Write an approximation algorithm to calculate the forth root
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0

user_input = int(input("Calculate the fourth root of: "))

while abs(ans ** 4 - user_input) >= epsilon:
    ans += increment
    
    num_guesses += 1
    
# print(f"ans: {ans}")
# print(f"Number of guesses: {num_guesses}")