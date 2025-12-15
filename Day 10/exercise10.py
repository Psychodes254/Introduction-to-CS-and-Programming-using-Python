def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    
    for i in range(len(Lf)):
        if not Lf[i](n):
            return False
        
    return True
     
def is_even(n):
    return n % 2 == 0

def greater_10(n):
    return n > 10 

def less_50(n):
    return n < 50

funcs = [is_even, greater_10, less_50]

user_input = int(input("Type a number: ")) 
print(all_true(user_input, funcs))