## EXAMPLE: successive addition
x = 0
for i in range(10):
    x += 0.125
print(x == 1.25)

#######

# 0.1 is not a perfect power of 2
x = 0
for i in range(10):
    x += 0.1
print(x == 1)

print(x, '==', 10*0.1)


## EXAMPLE
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print(f'Remainder = {str((2**p)*x - int((2**p)*x))}')
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print(f'The binary representation of the decimal {str(x)} is {str(result)}')


## EXAMPLE: Approximation by epsilon increments
x = 36
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')


# Suppose you are just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.
n = 0.022
N = 1
x = n
while x == n*N:
    print(x)
    x += n
    N += 1
    
print(f'count is {N-1} where {x-n} != {n*(N-1)}')