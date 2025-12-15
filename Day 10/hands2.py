# Write a function that meets the specification.

def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e.
    """
    new_list = []
    
    for i in L:
        if i != e:
            new_list.append(i)
            
    return new_list
    
    # for i in range(len(L)):
    #     if e in L:
    #         L.remove(e)
        
    # return L

    
L = [1,2,2,2]
print(remove_elem(L, 1)) # prints [1]