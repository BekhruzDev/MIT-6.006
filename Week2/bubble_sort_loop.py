def bubble_sort_loop(A):
    '''
    Strategy: Iterating and Swapping pairs
    Algorithm:
    1. Start iterating through all elements
    2. During iteration, Compare consecutive pairs of elements and swap them so that the smaller is first
    3. At the end of iteration, start over again
    4. Keep iterating untill no more swaps are needed
    '''
    size = len(A)
    swap = True
    while swap:
        swap = False
        print(A)
        for i in range(size - 1):
            if A[i] > A[i + 1]:
                A[i], A[i+1] = A[i+1], A[i]
                swap = True
        
    

#TEST
print("Test")
sample = [2,3,45,6,2,0,12,10,98,5,4,9]
bubble_sort_loop(sample)
