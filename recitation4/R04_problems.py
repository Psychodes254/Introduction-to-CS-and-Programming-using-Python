# Problem 1: Lamba Functions Practice
# a) Write a lambda function that calculates the cube root of a given number 
# passed in as an argument
f1 = lambda n: n ** (1/3)

# b) Write a lambda function that takes in two arguments and outputs the product
# of those two numbers. 
f2 = lambda x, y: x * y

# print(f1(8))
# print(f1(4))
# print(f2(1,2))
# print(f2(4,5))


# Problem 2: Practice working with Tuples:
# Write a function that counts the number of times the number 1 appears 
# in an inputted tuple.
def count_number_one(nums):
    count = 0
    for i in nums:
        if i == 1:
            count += 1
    return count

# print(count_number_one((1,2,3,4,5,1,1)))  


# Problem 3: Practice working with Python Tuples
# Write a Function that takes in two tuples and outputs a single tuple containing 
# only common elements of both tuples. 
def common_elements(tup1, tup2):
    new = []
    for elem1 in tup1:
        for elem2 in tup2:
            if elem1 == elem2:
                new.append(elem1)
    
    return tuple(new)

# print(common_elements((2,3,4), (3,4,5,6)))


# Problem 4: Practice working with Python Lists
# Write a Python program to remove sublists from a given list of lists, which 
# contain an element outside a given range.
def remove_list_range(elems, start, end):
    flat_list = []
    
    for elem in elems:
        flat_list.extend(elem)
         
    return flat_list[start:end]
        
# print(remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17))