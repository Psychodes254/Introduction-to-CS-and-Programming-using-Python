# Write code that satisfies the following specs

def is_palindrome(s):
    """ s is a string
    Returns True if s is a palindrome and False otherwise
    """
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome(str('abc')))

# For example:
#  If s = "222" returns True
#  If s = "2222" returns True
#  If s = "abc" returns False