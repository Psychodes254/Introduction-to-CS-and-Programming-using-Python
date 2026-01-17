## EXAMPLE: combinations of print and return
def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

# is_even_with_return(3)          # -> False
# print(is_even_with_return(3))  # -> print(False)

def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Returns None
    """
    print('without return')
    remainder = i % 2
    has_rem = (remainder == 0)
    print(has_rem)
    ##return None

# is_even_without_return(3)          # -> None
# print(is_even_without_return(3))  # -> print(None)


### EXAMPLE: bisection square root as a function
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x: 
            low = ans
        else: 
            high = ans
        ans = (high + low)/2.0
#    print(ans, 'is close to the root of', x)
    return ans

# print(bisection_root(4))
# print(bisection_root(123))


## Scope example: paste this into the Python Tutor
########################
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x

# x = 3
# z = f( x )


###########################
#### EXAMPLE: shows accessing variables outside scope
###########################
def f(y):
    x = 1
    x += 1
    print(x)
    
# # x = 5
# # f(x)
# # print(x)

def g(y):
    print(x)
    print(x+1)
    
# # x = 5
# # g(x)
# # print(x)

def h(y):
    x += 1 #leads to an error without line `global x` inside h

# # x = 5
# # h(x)
# # print(x)


## EXAMPLE: functions as parameters
def calc(op, x, y):
    return op(x,y)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b
    
def div(a,b):
    if b != 0:
        return a/b
    print("Denominator was 0.")

# print(calc(add, 2, 3))
# print(calc(div, 2, 0))


## trace the scope progression of this code
def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(f, z):
    print('inside func_c')
    return f(z)

# print(func_a())
# print(5 + func_b(2))
# print(func_c(func_b, 3))


# Write a function that takes in an int and two functions as 
# parameters (each takes in an int and returns a float). 
# It applies both functions to numbers between 0 and n (inclusive) 
# and returns the maximum value of all outcomes. 
def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    return max(n, f1(n), f2(n))

# print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


## Quizzes AT HOME 
def is_palindrome(s):
    """ s is a string
    Returns True if s is a palnidrome and False otherwise. 
    A palindrome is a string that contains the same 
    sequence of characters forward and backward """
    # Compare the reverse string action
    return s == s[::-1]

# For example:
# print(is_palindrome("222"))   # prints True
# print(is_palindrome("2222"))   # prints True
# print(is_palindrome("abc"))   # prints False


def f_yields_palindrome(n, f):
    """ n is a positive int
        f is a function that takes in an int and returns an int
    Returns True if applying f on n returns a number that is a
    palindrome and False otherwise.  """
    # Perform the function action
    func_int = f(n)
    
    # Perform the Palindrome function
    return is_palindrome(str(func_int))

# For example:
def f(x):
    return x+1

def g(x):
    return x*2

def h(x):
    return x//2

# print(f_yields_palindrome(2, f))   # prints True
# print(f_yields_palindrome(76, f))   # prints True
# print(f_yields_palindrome(11, g))   # prints True
# print(f_yields_palindrome(123, h))   # prints False
