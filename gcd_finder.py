def find_gcd_loop(a, b):
    '''
    Find the greatest common divisor of the 2 integers using loop
    '''
    while b>0:
        c = b
        b = a % b
        a = c
    return a

def find_gcd_rec(a, b):
    '''
    Find the greatest common divisor of the 2 integers using recursion
    '''
    if b == 0:
        return a
    return find_gcd_rec(b, a % b)
    
    
    
    
print(find_gcd_rec(24, 126))