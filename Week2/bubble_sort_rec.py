def bubble_sort_rec(A, n = None, swap = True):
    '''
    Algorithm: Iterating and Swapping pairs
    1. Keep swapping PAIR OF CONSECUTIVE elements with bigger one on the right
    2. Move the largest to A[n - 1], A[n - 2], A[n - 3] and so on 
    3. Keep passing swap boolean as extra argument to check if one more iteration is needed.
    
    '''
    print(A)
    if n is None: 
        n = len(A)
    if not swap or n == 1:
        return
    for i in range(n - 1):
        swap = False
        if A[i] > A[i + 1]:
            swap = True
            A[i], A[i + 1] = A[i + 1], A[i]
    bubble_sort_rec(A, n - 1, swap)


def bubble_sort_rec_v2(A, suffix_start = 1, swap = True):
    '''
    Recursive bubble_sort_rec() but with while loop within
    '''
    print(A)
    if not swap or suffix_start == len(A):
        return
    i = 0
    while i < len(A) - suffix_start:
        swap = False
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            swap = True
        i += 1
    bubble_sort_rec_v2(A, suffix_start + 1, swap)

#TEST
print("Test")
sample = [2,3,45,6,2,0,12,10,98,5,4,9]
bubble_sort_rec(sample)


        
        