# Write code that satisfies the following specs


def div_by(n, d):
    """ n and d are ints> 0
    Returns True if d divides n evenly and False otherwise """
    return n % d == 0
    
  
print(div_by(10, 3))
print(div_by(195, 13))