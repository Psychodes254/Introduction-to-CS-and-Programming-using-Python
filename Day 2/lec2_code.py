## STRINGS ##
a = 'me'
b = "myself"
c = a + b        # memyself
d = a + " " + b  # me myself
silly = a * 3    # mememe

s = "abc"
len(s)   # 3

## INDEXING ##
s = "abc"
s[0] # a
s[1] # b
s[2] # c
# s[3]  # this is an error
s[-1] # c
s[-2] # b
s[-3] # a

## SLICING ##
s = "abcdefgh"
s[3:6] # def
s[3:6:2] # df
s[:]   # abcdefgh
s[::-1] # hgfedcba
s[4:1:-2] # ec

## MANIPULATION ##
s = "car"
#s[0] = 'b'  # this is an error
s = 'b'+s[1:len(s)] # bar


## PRINTING ##
a = "the"
b = 3
c = "musketeers"
# print(a, b, c)  # the 3 musketeers
# print(a + b + c)   # this is an error
# print(a + str(b) + c)  # the3musketeers

num = 5
# print("my num is", num) # my num is 5
s = "my num is" + str(num)
# print(s)  # my num is5

x = 1
x_str = str(x)
# print("my fav num is", x, ".", "x =", x)  # my fav num is 1 . x = 1
# print("my fav num is " + x_str + ". " + "x = " + x_str)  # my fav num is 1. x = 1

## USER INPUT ##
# #Example 1
# text = input("Type anything... ")  # me
# print(5*text)  # mememememe

# #Example 2
# num1 = input("Type a number: ")  # 5
# print(5*num1)  # 55555
# num2 = int(input("Type a number: "))
# print(5*num2)  # 25


# Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run

# verb = input("Type a verb: ")
# print(f"I can {verb} better than you! \n{5*verb}")


# #Example 3 - Newton's Method for cube root
# x = int(input('What x to find the cube root of? '))  # 27
# g = int(input('What guess to start with? '))  # 4

# print('Current estimate cubed = ', g**3)  # 64
# next_g = g - ((g**3 - x)/(3*g**2))
# print('Next guess to try = ', next_g)  # 3.2291666666666665


# ## F-STRINGS ##
num = 3000
fraction = 1/3
# print(num*fraction, 'is', fraction*100, '% of', num)  # 1000.0 is 33.3333.. % of 3000
# print(num*fraction, 'is', str(fraction*100) + '% of', num)  # 1000.0 is 33.3333..% of 3000
# print(f'{num*fraction} is {fraction*100}% of {num}')  # 1000.0 is 33.3333..% of 3000

# print(f'{num*fraction:,.0f} is {fraction*100:,.2f}% of {num:,}')  # 1,000 is 33.33% of 3,000


pset_time = 15
sleep_time = 8
# print(sleep_time > pset_time)  # False
# derive = True
# drink = False
# both = drink and derive
# print(both)  # False


# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.
# import random

# is_true = False
# secret = random.randint(0, 10)
# user_input = int(input("Type a number: "))

# if user_input == secret:
#     is_true = True
    
# print(is_true)


# ## BRANCHING ##
# #Example 1
pset_time = 22
sleep_time = 8
# if (pset_time + sleep_time) > 24:
#     print("impossible!")
# elif (pset_time + sleep_time) >= 24:
#     print("full schedule!")
# else:
#     leftover = abs(24-pset_time-sleep_time)
#     print(leftover,"h of free time!")
# print("end of day")


# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
# else:
#     print("These are not equal!")


# ## NESTED BRANCHING ##
# #Example 1
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
# print("thanks!")


# What's printed when y = 2, y = 20, y = 11?
# What if "if x <= y:" becomes "elif x <= y:"

answer = ''
x = 11
y = 2 # try 20 and 11
if x == y:
    answer = answer + 'M'
elif x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
# print(answer)  # 2: T | # 20: i | # 11: M


# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 
# import random

# secret_no = random.randint(1, 100)
# user_guess = int(input("Guess a number between 1 - 100: "))

# if user_guess > secret_no:
#     print(f"\n{user_guess} is too high!")
# elif user_guess < secret_no:
#     print(f"\n{user_guess} is too low!")
# else:
#     print(f"\n{user_guess} is the same as the secret number!")


## AT HOME ##
# Practice 1: What is the value of s1 and s2?
s1 = "a" + "b"  # ab

d = "hi"
e = " ana"
s2 = d + 2*e  # hi ana ana

# Practice 2: What are the substrings of s?
s = "ABC d3f ghi"
s[0:3:1]  # ABC
s[0:4]   # ABC 
s[8:len(s):3]  # g
s[2::-1]  # CBA 


# Practice 3: What does this print?
answer = ''
x = 11
# try with y = 2 and y = 12
y = 2
if len(str(x)) == len(str(y)):
    if y != 0 and x%2 == 1:
        answer = answer + "x / y is " + str(x/y)
elif x < y:
    answer += "\nx is smaller"  # \n inserts a newline character in the string
else:
    answer += "\ny is smaller"
# print(answer)  # 2: y is smaller | # 12: x / y is 0.91666...


# What does it print when a = 6 and b = "6"  # int conversion, int and str conversion
# What does it print when a = "1" and b = 1  # interesting
# What does it print when a = 3 and b = 3  # int conversion, interesting
# What does it print when a = "1" and b = "1"  # interesting

# if ( a == int(b) ):
#     print("int conversion")
# if ( a == int(b) ) and ( str(a) == b ):
#     print("int and str conversion")
# else: 
#     print("interesting")
 