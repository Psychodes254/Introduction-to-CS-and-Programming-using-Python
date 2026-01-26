# EXAMPLE: while loops 
where = input("You are in the Lost Forest. Go left or right? ")
while where == "right":
    where = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest! \o/")


# Fun Lost Forest code, run it on your own!
where = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while where.lower() == "right":
   where = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯\n     ︵ \n    ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")


## EXAMPLE 
n = int(input('Please enter a non-negative integer: '))
while n > 0:
    print('x')
    n -= 1


## EXAMPLE: counter
## With while loop
n = 0
while n < 5:
    # print(n)
    n = n+1

## With for loop
for n in range(5):
   print(n)


## EXAMPLE: factorial
## With while loops
x = 6
i = 1
factorial = 1
while i <= x:
    factorial *= i
    i += 1
# print(f'{x} factorial is {factorial}')

## With for loops
factorial = 1
for i in range(1, x+1, 1):
    factorial *= i
# print(f'{x} factorial is {factorial}')


## EXAMPLE: sum
mysum = 0
for i in range(10):
   mysum += i
# print(mysum)

# mysum = 0
for i in range(7, 10):
   mysum += i
# print(mysum)

#mysum = 0
for i in range(5, 11, 2):
   mysum += i
   if mysum == 5:
       break
       mysum += 1
# print(mysum)


# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
for i in range(1, x+1):
    if i % 5 == 0:
        print(i)
        

# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits.
n = 4
total = 0
for i in range(n+1):
    total += i
print(total)