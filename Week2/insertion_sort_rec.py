def insertion_sort_rec(A, i):
    '''
    Strategy: Take a card from the deck on the table with your right hand, 
    and insert it into your left hand so that the card with the largest value is on the top
    Algorithm:
    
    '''
    print(A)
    if i is None:
        i = len(A)
    if i <= 0: return
    for j in range(i, len(A)):
        if A[j-1]>A[j]:
            A[j-1], A[j] = A[j], A[j-1]
    insertion_sort_rec(A, i-1)
    
#TEST
sample = [2,3,45,6,2,0,12,10,98,5,4,9]
insertion_sort_rec(sample, None)