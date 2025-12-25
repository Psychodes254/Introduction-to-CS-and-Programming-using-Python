# Modify the str method to represent the Fraction as just thenumerator, when the 
# denominator is 1. Otherwise itsrepresentation is the numerator then a / then the denominator.

class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.denom)

# Example:
a = Fraction(1,4)
b = Fraction(3,1)
print(a) # prints 1/4
print(b) # prints 3