'''
c part of problem session 2. This c part includes solutions to the a and b parts as well.

Input: H | list of bricks per house from west to east
Output: D | list of damage per house from west to east

Algorithm: Find the number of items(integers) less than A[i] that are among the items after A[i] in O(nLogn)
Hint: Solve by modifying the merge_sort algorithm 
'''

def get_damages(H):
    D = [1 for _ in H]
    H2 = [(H[i], i) for i in range(len(H))]
    def merge_sort(A, a = 0, b = None):
        if b is None: b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            i,j = 0,0
            L,R = A[a:c],A[c:b]
            while a < b:
               if j>=len(R) or (i < len(L) and L[i][0] <= R[j][0]):
                   D[L[i][1]] += j       #cuz, all items till j-th item are less than i-th item
                   A[a] = L[i]
                   i += 1
               else:
                   A[a] = R[j]
                   j += 1
               a += 1        

    merge_sort(H2)
    return D
    
#Test
H = [2,3,45,6,2,0,12,10,98,5,4,9,100]
print(H)
print(get_damages(H))     
        
        