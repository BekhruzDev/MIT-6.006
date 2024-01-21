def merge_sort(A, a, b = None):
    '''
    Strategy: Divide into 2 halves and Conquer by merging 2 subarrays!
    Time Complexity: O(n * logn), n is for merging the halves and logn is the number of steps
    '''
    if b is None:
        b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2  # +1 for efficiency purposes
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        i, j = 0, 0
        while a < b: # O(n), 2-finger rule
            if j >= len(R) or (i < len(L) and L[i] < R[j]):
                A[a] = L[i]
                i += 1
            else:
                A[a] = R[j]
                j += 1
            a += 1
            print("Left: ", L, "Right: ", R, '\n')

            
            
#TEST
sample = [2,3,45,6,2,0,12,10,98,5,4,9,100]
merge_sort(sample, 0, None)
print("Finally:", sample)


        