def direct_access_array_sort(A):
    '''
    Algorithm: 
    1. Create a DAA of size u, where u >= n (n is #items)                     -> O(u)
    2. Insert all items from A into DAA so that the DAA indices = item keys   -> O(n)
    3. Now, in DAA, all items are in sorted order
    4. Insert all items from DAA back to A, leaving out the empty spaces in DAA -> O(u)
    
    Drawbacks:
    1. DAA can't handle duplicate keys
    2. DAA can't handle large key spaces
    '''
    
    u = 1 + max([x.key for x in A])
    DAA = [None] * u
    
    for x in A:
        DAA[x.key] = x
        
    for key in range(u):
        if DAA[key] is not None:
            A[key] = DAA[key]
    return A