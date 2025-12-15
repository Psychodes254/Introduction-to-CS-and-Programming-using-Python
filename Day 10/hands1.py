# Write a function that meets these specs:
    
def make_ordered_list(n):
    """ n is a positive int
    Returns a list containing all intsin order
    from 0 to n (inclusive)
    """
    order = []
    
    for i in range(n+1):
        order.append(i)
        
    return order

print(make_ordered_list(8))