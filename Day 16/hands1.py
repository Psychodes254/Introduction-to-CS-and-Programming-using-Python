# Sum of the elememts in a list using recursion

def total_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + total_recur(L[1:])

test = [30, 40, 50]
print(total_recur(test))