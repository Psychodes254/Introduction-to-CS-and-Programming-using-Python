def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    
    # Initiate new List
    new_list = []  
    
    # Iterate through keys and values
    for k, v in aDict.items():
        
        # Check if tha value corresponds to the target, then add respective key to teh new list
        if v == target:
            new_list.append(k)
     
    # Sort the new list while handling the strings incase they are included
    new_list.sort(key=lambda v: (isinstance(v, str), v))
      
    # Return the new list
    return new_list

# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target)) # prints the list [1,5]