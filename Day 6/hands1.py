# Write code to do bisection search to find the cube root of
# positive cubes within some epsilon. Start with:
    
cube = 27
epsilon = 0.01
low = 0
high = cube

guess = (high + low) / 2

while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 > cube:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
print(f"{guess} is the cube root of the number")