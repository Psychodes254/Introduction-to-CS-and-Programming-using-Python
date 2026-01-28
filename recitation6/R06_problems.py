# Problem 1: List concatenation
original_list = [1,2,35,10,5,8,9,23]

# a) Using List concatenation create a new list from the orignal list, 
# removing all multiples of 5 from a list of numbers.
mult_five = [x for x in original_list if x % 5 != 0]
print(mult_five)

# b) Using list concatenation create a new list from the original list, 
# where each element is half the original element
half_elme = [(x/2) for x in original_list]
print(half_elme)


# Problem 2: Write a Function to insert a specified element x in a given list 
# after every nth element.
def insert_element_list1(lst, x, n):
    """
    Parameters:
    lst: input list
    x: element to insert
    n: x will be inserted after every nth element
    Returns: new modified list 
    """
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[i])
        if (i+1) % n == 0:
            new_list.append(x)
    return new_list

nums = [1, 3, 5, 7, 9, 11,0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
x = 20
n = 4
print(insert_element_list1(nums, x, n))


# Problem 3: Write a Function to sort list of lists containing integers such that the 
# sub-lists are sorted in increasing order. How would you sort in decreasing order?
def sort_list_of_lists(lst):
    """
    Parameters:
    lst: input list
    n: index to sort by
    Returns: the sorted list 
    """
    return [(sorted(elem)) for elem in lst]

items = [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
print(sort_list_of_lists(items))


# Problem 4: Write a Function to split a given list into size n chunks 
# using list comprehension. If the list does not divide equally, the last 
# chunk should be short. Return the new list. 
def split_list(lst, n):
    """
    Parameters:
    lst: input list
    n: size of chunks
    Returns: new split list 
    """
    return [lst[i:i + n] for i in range(0, len(lst), n)]

nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
n = 4
print(split_list(nums,n))
n = 5
print(split_list(nums,n))