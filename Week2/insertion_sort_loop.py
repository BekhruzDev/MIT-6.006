def insertion_sort_loop(A):
    '''
    Strategy: Take a card from the deck on the table with your right hand, 
    and insert it into your left hand so that the card with the largest value is on the top
    Algorithm: 
    1. Start iterating from the second element (iterating forward ->>)
    2. Check if it is larger than the element in it's left side, if not swap the elements, and do this over till the first element (<<- iterating backward)
    Time Complexity: O(n^2)
    '''
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
        print(A)
                
                
#TEST
sample = [2,3,45,6,2,0,12,10,98,5,4,9]
insertion_sort_loop(sample)
