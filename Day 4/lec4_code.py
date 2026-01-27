mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)


## EXAMPLE: looping over characters
## These 3 code snippets do the same thing
s = "demo loops - fruit loops"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")
      
s = "demo loops - fruit loops"
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")

s = "demo loops - fruit loops"
for char in s:
    if char in 'iu':
        print("There is an i or u")


## EXAMPLE:  robot cheerleaders
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for w in word:
    if w in an_letters:
        print(f'Give me an {w}: {w}')
    else:
        print(f'Give me a {w}: {w}')
print("What does that spell?")
for i in range(times):
    print(word, "!!!")


## EXAMPLE: guessing perfect square roots
x = int(input("Enter an integer: "))
guess = 0
while guess**2 < x:
    guess += 1
if guess**2 == x:
    print(f'Square root of {x} is {guess}')
else:
    print(f'{x} is not a perfect square')


## EXAMPLE:  square root with negative flag
guess = 0
neg_flag = False
x = int(input("Enter a positive integer: "))
if x < 0:
    neg_flag = True
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print(f'Square root of {x} is {guess}')
else:
    print(f'{x} is not a perfect square')
    if neg_flag:
        print(f'Just checking... did you mean {-x} ?')


## EXAMPLE:  cube root
# finding a perfect cube of positive numbers
cube = int(input("Enter an integer: "))
for guess in range(cube+1):
    if guess**3 == cube:
        print(f'Cube root of {cube} is {guess}')

# finding perfect cube with negative numbers
cube = int(input("Enter an integer: "))
for guess in range(abs(cube)+1):
    if guess**3 == abs(cube):
        if cube < 0:
            guess = -guess
        print(f'Cube root of {str(cube)} is {str(guess)}')
        
# finding cube root with error message
cube = int(input("Enter an integer: "))
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(f'{cube} is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print(f'Cube root of {str(cube)} is {str(guess)}')


# EXAMPLE: word problems
# this code is very slow for large numbers!
for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total = (alyssa + ben + cindy == 10)
            two_less = (ben == alyssa-2)
            twice = (cindy == 2*alyssa)
            if total and two_less and twice:
                print(f"Alyssa sold {alyssa} tickets")
                print(f"Ben sold {ben} tickets")
                print(f"Cindy sold {cindy} tickets")

# this code is better -- only one loop!
for alyssa in range(1001):
    ben = max(alyssa-20,0)
    cindy = alyssa*2
    if ben + cindy + alyssa == 1000:
        print(f'Alyssa sold {alyssa} tickets')
        print(f'Ben sold {ben} tickets')
        print(f'Cindy sold {cindy} tickets')


# EXAMPLE: floating point
x = 0
for i in range(10):
    x += 0.1
print(x == 1)
print(x, 'is the same as?', 10*0.1)


## EXAMPLE: Convert to binary
## Only positive numbers
num = 1507
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
print(result)

## Can handle negative numbers
num = -15
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False
results = ''
if num == 0:
    results = '0'
while num > 0:
    results = str(num%2) + results
    num = num//2
if is_neg:
    results = '-' + results
print(results)


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


## EXAMPLE: successive addition
x = 0
for i in range(10):
    x += 0.125
print(x == 1.25)

#######

x = 0
for i in range(10):
   x += 0.1
print(x == 1)

print(x, '==', 10*0.1)


# Write code that counts how many unique common characters there are between 
# two strings.
text1 = "may the fourth be with you"
text2 = "revenge of the sixth"
count2 = 0
new_list = ''
for elem1 in text1:
    if elem1 in text2:
        if elem1 not in new_list:
            count2 += 1
print(count2)
