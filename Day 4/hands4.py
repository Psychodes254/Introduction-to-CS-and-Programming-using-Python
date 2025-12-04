# Guess and check

guess = 0

neg_flag = False

x = int(input("Type a number: "))

if x < 0:
    neg_flag = True
while guess ** 2 < x:    
    guess += 1
if guess ** 2 == x: 
    print(f"{guess} is the square root of {x}.")
else:
    print(f"{x} is not a perfect square.")
    if neg_flag:
        print(f"Did you mean {-x}?")
         
    