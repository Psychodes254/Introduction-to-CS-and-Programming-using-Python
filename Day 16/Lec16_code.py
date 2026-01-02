# Fibonacci with a dictionary 
def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-2)

# Example:
# print(fib_recur(34))


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

# Example:
d = {1:1, 2:1}
# print(fib_efficient(34, d))


def score_count(x):
    """ Returns all the ways to make a score 
    of x by adding 1, 2, and/or 3 together. 
    Order doesn't matter. """
    if x == 1:
        return 1  # 1+0
    elif x == 2:
        return 2  # 2+0 or 1+1
    elif x == 3:
        return 3  # 3+0 or 2+1 or 1+1+1
    else:
        # make a score of x-1 then add 1
        # and make a score of x-2 then add 2
        # and make a score of x-3 then add 3
        return score_count(x-1)+score_count(x-2)+score_count(x-3)
 
# Examples:
# print(score_count(4))  # prints 6
# print(score_count(6))  # prints 20
# print(score_count(13))  # prints 1431


## sum of a list, iterative
def total_iter(L):
  result = 0
  for e in L:
    result += e
  return result

test = [30, 40, 50]
# print(total_iter(test))


## sum of a list, recursive
def total_recur(L):
  if L == []:
    return 0
  else:
    return L[0] + total_recur(L[1:])

# Example:
test = [30, 40, 50]
# print(total_recur(test))


## is an element in a list?
## incorrect
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:    
        return in_list(L[1:], e)

# Examples:
test = [2,5,8,1]
# print(in_list(test, 0))  # good

test = [2,5,8,1]
# print(in_list(test, 1))  # good

test = [2,1,5,8]
# print(in_list(test, 1))  # bad!


## is an element in the list
## correct (look at the first elem in the list)
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:    
        if L[0] == e:
            return True
        else:
            return in_list(L[1:], e)


## another correct (look at the last elem in the list)
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:    
        if L[-1] == e:
            return True
        else:
            return in_list(L[:-1], e)
      
        
## another correct and simplified implementation
def in_list(L, e):
    if len(L) == 0:
        return False
    elif L[0] == e:
        return True
    else:
        return in_list(L[1:], e)

# Examples:
test = [2,5,8,1]
# print(in_list(test, 1))

test = [1,2,5,8]
# print(in_list(test, 1))

test = [2,5,8]
# print(in_list(test, 1))


## flatten a list containing sublists of ints
def flatten(L):
    """ 
    L is a list containing lists with integer elements
    Returns a list containing elements that are the 
    integers in the sublists of L in the same order.
    """
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + flatten(L[1:])
 
# Examples:
test = [[1]]
# print(flatten(test))

test = [[1,2], [3,4], [9,8,7]]
# print(flatten(test))


## reverse a list's elements
def my_rev(L):
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]]

# Exmaples:
# test = [1, 2, "abc"]
# print(my_rev(test))

# test = ["abc", ['d'], ['e', ['f', 'g']]]
# print(my_rev(test))


## reverse a list's elements (and its list elems, etc, recursively)
def deep_rev(L):
    if len(L) == 1:
        if type(L[0]) != list:
            return L
        else:
            return [deep_rev(L[0])]
    else:
        if type(L[0]) != list:
            return deep_rev(L[1:]) + [L[0]]
        else:
            return deep_rev(L[1:]) + [deep_rev(L[0])]

# Examples:
# test = [1, 2, "abc"]
# print(my_rev(test))

# test = ["abc", ['d'], ['e', ['f', 'g']]]
# print(deep_rev(test))


## cleaned up code to reverse a list's elements (and its list elems, etc, recursively)
def deep_rev(L):
  if L == []:
    return L
  elif type(L[0]) != list:
    return deep_rev(L[1:]) + [L[0]]
  else:
    return deep_rev(L[1:]) + [deep_rev(L[0])]

# Examples:
# test = [1, 2, "abc"]
# print(my_rev(test))

# test = ["abc", ['d'], ['e', ['f', 'g']]]
# print(deep_rev(test))



## EXTRA CONTENT: towers of hanoi
def print_move(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

# Example:
# towers(4, 'a', 'b', 'c')


# Q1.
def score_count(x, d):
    count = 0
    
    if x == 0:
        return 1
    if x in d:
        return d[x]
    
    for points in d:
        count += score_count(x - points, d)
      
    return count

# Examples:            
d = {1:1, 2:2, 3:3}
# print(score_count(4, d))  # prints 6
# print(score_count(6, d))  # prints 20
# print(score_count(13, d))  # prints 1431

# Q2. 
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or 
    sublists of L and False otherwise. 
    """
    if len(L) == 1 and type(L[0]) != list:
        return e == L[0]
    elif len(L) == 1 and type(L[0]) == list:
        return e in L[0]
    elif type(L[0]) == list:
        if e in L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)
    elif type(L[0]) != list:
        if e == L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)

# Examples:
test = [[1,2],3,4,5,6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 10))  # prints False


# Q3.
def my_deepcopy(L):
    """ 
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that 
    contains copies (recursively) of every sublist 
    """
    if len(L) == 0:
        return []
    elif type(L[0]) != list:
        return [L[0]] + my_deepcopy(L[1:])
    else:
        return [my_deepcopy(L[0])] + my_deepcopy(L[1:])

# Examples:
myL = ["abc", ['d'], ['e', ['f', 'g']]]
my_newL = my_deepcopy(myL)
# print(myL)
# print(my_newL)
# myL[2][1][0] = 1
# print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
# print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]


# Q4.
def f(L):
    """ L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet. """
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < f((L[0])):
            return L[0]
        else:
            return L[1]

# Example:        
# print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a'


# Q5.
def g(L, e):
    """ L is list of ints, e is an int
    Returns a count of how many times e occurrs in L  """
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            return 1 + g(L[1:], e)
        else:
            return g(L[1:], e)

# Examples:
# print(g([1,2,3,1], 1))     # should print 2
# print(g([1,1,2,3,1,1], 1)) # should print 4
    

# Q6.
def h(L, e):
    """ L is list, e is an int
    Returns a count of how many times e occurrs in L or 
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    else:
        if type(L[0])==int:
            if L[0] == e:
                return 1+h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0])== list:
            return h(L[0], e) + h(L[1:], e)

# Examples:    
# print(h([1,2,[3],1], 1))        # should print 2
# print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4
