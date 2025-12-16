# Make a copy to save the elements. The use L.clear() to empty out the 
# list and repopulate it with the ones you’re keeping.

def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    new_list = []
    for i in L:
        if i != e:
            new_list.append(i)
            
    L.clear()
    L[:] = new_list
            

L = [1,2,2,2]
remove_all(L, 2)
print(L) # prints [1]