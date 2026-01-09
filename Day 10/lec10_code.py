## EXAMPLE: change value in a list and appending a value to a list
L = [2, 4, 3]
# print(L)
L[1] = 5
# print(L)
L = L.append(5) # None
# print(L)


# What is the value of L1, L2, L3, and L after these commands?
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.append(L4)   
# print(L3)      # ['do', ['re', 'mi']]
L = L2.append(L3)  # None
# print(L)


## EXAMPLE: string-list ops
s = "I<3 cs and u?"		
L = list(s) 	
L1 = s.split(' ')	
L2 = s.split('<')
# print(L)
# print(L1)
# print(L2)

L = ['a','b','c']
A = ''.join(L)	
# print(A)
B = '_'.join(L)	
# print(B)

Lnum = [1, 2, 3]
# n = ''.join(Lnum)  # this line throws an error
Lnum = ['1', '2', '3']
n = ''.join(Lnum)
# print(n)


## EXAMPLE: sorting/reversing ops
L=[9,6,0,3]
a = sorted(L)
# print(a)
# print(L)
a = L.sort()
# print(a)  # None
# print(L)
L.reverse()
# print(L)


## Loops over lists
def square_list(L):
    for i in range(len(L)): 
        L[i] = L[i]**2

# print(square_list([2,3,4]))  # prints None
Lin = [2,3,4]
# print("before fcn call:",Lin)
square_list(Lin)
# print("after fcn call:",Lin)   # mutated L


## TRICKY EXAMPLE 1: append to L while iterating over range(L)
L = [1,2,3,4]
for i in range(len(L)):
    L.append(i) 
    # print(L)


## TRICKY EXAMPLE 2: append to L while iterating over L
## this leads to an infinite loop
# L = [1,2,3,4]
# i = 0
# for e in L:
#     L.append(i)
#     i += 1
#     print(L)


## extend a list
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
L1.extend([0,6])
L2.extend([[0,2],[7,9]])
# print(L1)
# print(L2)
# print(L3)


## TRICKY EXAMPLE 3: combining
L = [1,2,3,4]
for e in L:
    L = L + L
    # print(L)


## Clear a list and check that it's the same object
L = [4,5,6]
# print(L)
# print(id(L))
L.clear()
# print(L)
# print(id(L)) # same as 3 lines up, same object

## vs.

L = [4,5,6]
# print(L)
# print(id(L))
L = []
# print(L)
# print(id(L))  # different than 3 lines up, different object!


############ AT HOME ###############
## Question 1
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.extend(L4)  # ['do', 're', 'mi']
L3.sort()      # ['do', 'mi', 're']
del(L3[0])     # ['mi', 're']
L3.append(['fa', 'la'])
# What's the value of L3 here?  # ['mi', 're', ['fa', 'la']]


## Question 2
L1 = ['bacon', 'eggs']
L2 = ['toast', 'jam']
brunch = L1        # ['bacon', 'eggs']
L1.append('juice') # ['bacon', 'eggs', 'juice']
brunch.extend(L2)
# What's the value of brunch here?  # ['bacon', 'eggs', 'juice', 'toast', 'jam']


## Question 3. 
def apply_to_each(L, f):
    """ L is a list of numbers 
        f is a list that takes in a number and returns a number
    Mutate L such that you apply function f to every element in L """
    new_list = []
    
    for num in range(len(L)):
        L[num] = f(L[num])
    return new_list

test = [1,-2,3]
apply_to_each(test, lambda x: x**2)
# print(test)   # prints [1,4,9]

test = [-7, 8, 5, -8, -3]
apply_to_each(test, abs)
# print(test)   # prints [7, 8, 5, 8, 3]
