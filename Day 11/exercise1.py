def remove_and_sort(Lin, k):
    """ 
    Lin is a list of ints, k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    
    # Create a slice copy after removing first k elements
    lin_copy = Lin[k:]
    
    # Clear the original list
    Lin.clear()
    
    # Copies elements from lin_copy back into Lin
    Lin[:] = lin_copy
    
    # Sorts the remaining elements in ascending order
    Lin.sort()

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]