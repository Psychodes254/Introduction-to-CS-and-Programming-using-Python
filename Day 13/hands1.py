def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    Returns a new list whose elements are the pairwise
    division of an element in Lnumby an element in Ldenom.
    Raise a ValueError if Ldenom contains 0. """
    
    assert len(Lnum) != 0 and Ldenom != 0, "L is empty"
    assert len(Lnum) == len(Ldenom), "length must be equal"
     
    div_pair = []
    for i in range(len(Lnum)):
        try:
            div_pair.append(Lnum[i] / Ldenom[i])
        except:
            raise ValueError("Can't divde 0 digit!")
        
    return div_pair
            
            

# Examples:
# L1 = [4,5,6]
# L2 = [1,2,3]
# print(pairwise_div(L1, L2)) # prints [4.0,2.5,2.0]

# L1 = [4,5,6]
# L2 = [1,0,3]
# print(pairwise_div(L1, L2)) # raises a ValueError, zero division

# L1 = []
# L2 = []
# print(pairwise_div(L1, L2)) # raises AssertionError, empty list

# L1 = [8, 9, 4,]
# L2 = [4, 2]
# print(pairwise_div(L1, L2)) # raises AssertionError, len not equal
