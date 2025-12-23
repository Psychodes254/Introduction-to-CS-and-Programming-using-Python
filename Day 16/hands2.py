# Modify the code we wrote to return the total length of all strings inside L:
    
def total_len_recur(L):
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])
    
    
test = ["ab", "c", "defgh"]

print(total_len_recur(test)) # prints 8