# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
# Hint: use a loop that increments a counter—you decide when the counter should stop.

perfect_cube = False
number = int(input("Type a number: "))

for n in range(abs(number+1)):
    if n ** 3 == abs(number):
        print(f"{number} is a perfect cube of {n}!")
        perfect_cube = True
    
if not perfect_cube:
    print("error!")