def selection_sort_rec(A, i = None):
    '''
    Strategy: Divide the given elements into UNSORTED part and SORTED part(initially empty), and fill SORTED part RECURSIVELY
    Algorithm:
    1. Find a largest number in prefix A[:i + 1] (using prefix_max())
    2. Swap that number with A[i]
    3. And now recursively sort A[:i], A[:i-1], A[:i-2] and so on till i = 0
    
    Time Complexity: O(n^2)
    '''
    print(A)
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort_rec(A, i - 1)


def prefix_max(A, i):
    '''
    Returns the index of the largest element among all elements till index i (excluding i)
    Time Complexity: O(n)
    NOTE: This algorithm is recursive and does not use any loop invarient to keep the max value(which is cool!)
    '''
    if i > 0:
        j = prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
    return i


#test
sample = [2,3,45,6,2,5,4,9]
print(sample)
selection_sort_rec(sample, None)
print(sample)