def apply(criteria, n):
    """ criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria 
    (i.e. return True when criteria is applied to them)
    """ 
    count = 0
    for i in range(0, n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x%2==0

def is_5(x):
    return x==5

# print('apply with is_5:',apply(is_5, 10))  # 1
# print('apply with anon fcn:', apply(lambda x: x==5, 100))  # 1


# # Shown another way, the following are equivalent:
# print(is_even(8))              # returns True
# print((lambda x: x%2==0)(8))  # returns True


# # 1. What does this print?
# print(apply(lambda x: x%2==0, 10))  # 6

# 2. Call apply on n=100 and a lambda func 
#    that takes in a parameter and returns 
#    whether the parameter is a multiple of 10
#    What does it print?
# print((lambda x: x%10 == 0) (100))  # True
# print(apply((lambda x: x%10 == 0), (100)))  # 11


def do_twice(n, fn):
    return fn(fn(n))

# print(do_twice(3, lambda x: x**2))


### example with returning a tuple with many values
def quotient_and_remainder(x, y):
      q = x // y
      r = x % y
      return (q, r)

# result = quotient_and_remainder(10,3)
# print(result)

# (quot, rem) = quotient_and_remainder(5,2)
# print('quotient is:', quot)
# print('remainder is:', rem)


### example of variable number of arguments
def mean(*args):
    """
    Assumes at least one argument and all arguments are numbers. 
    Returns the mean of the arguments.
    """
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

# print(mean(1,2,3,4,5,6))  # 3.5
# print(mean(6,0,9))        # 5.0


## Compare above code with this one:
# Note args vs *args and mean((6,0,9)) vs mean(6,0,9)
def _mean(args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

# print(_mean((1,2,3,4,5,6)))   # 3.5
# print(_mean((6,0,9)))         # 5.0

 
## EXAMPLE: sum element values in a list 
def list_sum(L):
    total = 0 
    for e in L: 
        total += e 
    return(total)

# print(list_sum([1,3,5]))  # 9


## EXAMPLE: sum lengths of string elements
def len_sum(L):
    total = 0 
    for s in L: 
        total += len(s) 
    return(total)

# print(len_sum(['ab', 'def', 'g']))   # 6


##Quizzes AT HOME 
# Trace this code:
# Figure out what it returns and then run it to check yourself.
def always_sunny(t1, t2):
    """ t1, t2 are non-empty """
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)

# print(always_sunny(('cloudy' ), ('cold',)))  # returns what?  ("sunny", "ccold")


def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    return max(n, f1(n), f2(n))

# print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


def sublist_sum(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    all_sum = 0
    for elem in L:
        for i in elem:
            all_sum += i
    return all_sum

# print(sublist_sum([[1,2], [4,5,6]])) # prints 18
