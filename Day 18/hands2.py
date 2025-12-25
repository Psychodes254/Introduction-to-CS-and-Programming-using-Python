# Implement the missing get_inverse and invert methods below

class SimpleFraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        
    def get_inverse(self):
        """ Returns a float representing 1/self """
        return self.denom / self.num
    
    def invert(self):
        """ Sets self's num to denom and vice versa. Returns None. """
        invert = self.num
        self.num = self.denom
        self.denom = invert
    
# Example:
f1 = SimpleFraction(3,4)
print(f1.get_inverse()) # prints 1.33333333 (note this one returns value)
f1.invert() # acts on data attributes internally, no return
print(f1.num, f1.denom) # prints 4 3
