def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    
    # Initiate an empty list
    new_list = []

    # Iterate through keys and values
    for k, v in d.items():
    # Sum the values, if positive add their respective key to the new list
        total_values = sum(v)
        if total_values > 0:
            new_list.append(k)
    
    # Sort the new list
    new_list.sort()
    
    # Return the new list 
    return new_list

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]