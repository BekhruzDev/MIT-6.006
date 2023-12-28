
def selection_sort_loop(A):
    '''
    Strategy: Divide the given elements into UNSORTED part and SORTED part(initially empty), and fill SORTED part ITERATIVELY
    Algorithm: 
    1. Find the maximum element and swap it with the last item
    2. Again the in remaining unsorted part, find the max element and swap it with the second last item
    3. Do this iteratively
    Time Complexity: O(n^2)
    '''
    size = len(A)
    sorted_start = size - 1
    while sorted_start > 0:
        for i in range(sorted_start, -1, -1):
            if A[i] > A[sorted_start]:
                A[sorted_start], A[i] = A[i], A[sorted_start]  
        sorted_start -= 1


def selection_sort_loop_v2(A):
    '''
    Strategy: Divide the given elements into SORTED part(initially empty) and UNSORTED part, and fill SORTED part ITERATIVELY
    Algorithm: 
    1. Find the minimum element and swap it with the first item
    2. Again the in remaining unsorted part, find the minimum element and swap it with the second item
    3. Do this iteratively
    Time Complexity: O(n^2)
    '''
    unsorted_start = 0
    size = len(A)
    while unsorted_start < size - 1:
        for i in range(unsorted_start, size):
            if A[i] < A[unsorted_start]:
                A[unsorted_start], A[i] = A[i], A[unsorted_start]  
        unsorted_start += 1
            

#TEST1
print("Test 1")
sample = [2,3,45,6,2,0,12,10,98,5,4,9]
print(sample)
selection_sort_loop(sample)
print(sample)

#TEST2
print("Test 2")
sample = [2,3,45,6,2,0,12,10,98,5,4,9]
print(sample)
selection_sort_loop_v2(sample)
print(sample)