def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    
    # Initiate an empty list
    results = []
    
    # Check each element in the list
    for i in range(len(L)):
        
        # Check if the element is a list, extend, else append the values to results
        if isinstance(L[i], list):
            results.extend(flatten(L[i]))
        else:
            results.append(L[i])
             
    return results

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]