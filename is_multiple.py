# Checks if n / m produces no remainders. If no remainders, then it is a multiple
def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False
    
print(is_multiple(2, 8))