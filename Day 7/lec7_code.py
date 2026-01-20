## EXAMPLE: applying functions to repeat same task many times
# A very simple example of a function that has one argument and returns one value
def is_even(i):   
    """Assumes: i, a positive int
    Returns True if i is even, otherwise False"""
    if i%2 == 0:
        return True
    else:
        return False
    
# print(is_even(3)) # <- prints False
# print(is_even(8)) # <- prints True


# # Using the is_even function later on in the code
# print("Numbers between 1 and 10: even or odd")

# for i in range(1,10):
    # if is_even(i):
        # print(i, "even")
    # else:
        # print(i, "odd")


### EXAMPLE: sum of all odd numbers between (including) a and b with a for loop
def sum_odd(a, b):
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2 == 1:
            sum_of_odds += i
            print(i, sum_of_odds)
    return sum_of_odds

# print(sum_odd(2,4)) 
# print(sum_odd(2,7)) 

# # with a while loop
def sum_of_odd(a, b):
    sum_of_odds = 0
    i = a
    while i <= b:
        if i%2 == 1:
            sum_of_odds += i
        i += 1
    return sum_of_odds

# print(sum_of_odd(2,4)) 
# print(sum_of_odd(2,7)) 


################ YOU TRY IT AT HOME #####################
# 1. Write code that satisfies the following specs:
def keep_consonants(word):
    """ word is a string of lowercase letters
        Returns a string containing only the consonants 
        of word in the order they appear
    """
    vowels = 'a,e,i,o,u'
    results = ''
    
    for char in word:
        if char not in vowels:
            results += char
    return results

# For example
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs


# 2. Write code that satisfies the following specs:
def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    if c not in s:
        return -1
    
    for i in range(len(s)):
        if s[i] == c:
            break
        
    for j in range(len(s)-1, -1, -1):
        if s[j] == c:
            break
        
    return j - i
            

# For example
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('xyz', 'b'))  # prints -1
