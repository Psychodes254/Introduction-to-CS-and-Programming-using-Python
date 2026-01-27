# Problem 1: Given a list of numbers. Write a function to turn every item of 
# a list into its square.
def square_list(my_list):
    new_list = []
    for val in my_list:
        new_list.append(val**2)
    return new_list

# print(square_list([1, 2, 3, 4]))
# print(square_list([10, 12, 13]))


# Problem 2: Write a Python program to concatenate element-wise 
# three given lists of same length
def concatenate_lists(list_a, list_b, list_c):
    new_list = []
    for elem in range(len(list_a)):
        new_list.append(list_a[elem] + list_b[elem] + list_c[elem])
    return new_list

list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']

# print(concatenate_lists(list1, list2, list3))


# Problem 3: Write a function to shift a given list to the right or left 
# direction by a specified amount.
def rotate_list(input_list, direction, shift):
    shift = shift % len(input_list)
    if direction == "right":
        return input_list[-shift:] + input_list[:-shift]
    elif direction == "left":
        return input_list[shift:] + input_list[:shift]
    else:
        raise ValueError("Not the correct direction!")
    
# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(rotate_list(input_list, "right", 14))
# print(rotate_list(input_list, "left", 4))


