# Write a function that meets these specs:
# Hint:rememberhowtocheckifacharacterisinastring?

def char_counts(s):
    """
    s is a string of lowercase charsReturn a tuple where 
    the first element is the number of vowels in s and 
    the second element is the number of consonants in s 
    """
    
    vowels = "aeiou"
    x = 0
    y = 0
    
    for char in s:
        if char in vowels:
            x += 1
        else:
            y += 1
            
    return(x, y)

print(char_counts("abcd"))