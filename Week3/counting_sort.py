def counting_sort(A):
    '''
    The same as Direct Access Array sort and can also handle duplicate keys using chains at the indices, just like hash tables.
    To keep the sort stable, the chain should have queue behaviour. First In First Out!
    
    Note: if u (key space) is smaller or linear, then overall run time of the algorithm will linear, O(n)
    else it is O(u+n)
    
    '''
    
    u = 1 + max([x.key for x in A])  #O(n)
    D = [[] for _ in range(u)]       #O(u) 
    for x in A:                      #O(n)
        D[x.key].append(x)
    
    i = 0
    for chain in D:                 #O(u), even if it is a nested loop, since n is kinda distributed over u s
        for x in chain:
            A[i] = x
            i += 1
            
    return A

#TODO: implement the couting sort using cumulative sums tmwr.

    

    