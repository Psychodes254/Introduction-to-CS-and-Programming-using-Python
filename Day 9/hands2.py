# Write a function that meets these specs:
def sum_and_prod(L):
    """
    L is a list of numbers Return a tuple where the first value is the sum of 
    all elements in L and the second value is the product of all elements in L
    """
    
    add, prod = (0, 1)
    
    for n in L:
        add += n 
        prod *= n
        
    return(add, prod)
            
print(sum_and_prod([2, 4, 6]))