# Complete the function that calculates n^p for variables n and p
def power_recur(n, p):
    # Handle base cases
    if p == 1:
        return n
    if p <= 0:
        return 1
    
    # Recursive Case: Call the function with a smaller power (n-1)
    else:
        return n * power_recur(n, p-1)
    
print(power_recur(2, 8))
