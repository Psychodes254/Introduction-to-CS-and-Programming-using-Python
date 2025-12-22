def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    # Handle base cases
    if exp == 1:
        return base
    if exp <= 0:
        return 1
    
    # Use divide-and-conquer approach
    if exp % 2 == 0: 
        # Handle even powers (exp//2)
        half = recur_power(base, exp // 2)
        return half * half
    
    # Handle odd powers
    else:
        return base * recur_power(base, exp - 1)

# Examples:
print(recur_power(2, -5))  # prints 32