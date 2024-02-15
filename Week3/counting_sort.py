import random


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

def counting_sort_cumulative(A):
    '''
    The same as counting_sort(), but cumulates the number of keys at each index of DAA.
    Then, orders the keys based on the values at DAA[key] and decrements it's number, DAA[key] -= 1
    Overall, runtime = O(u + n)
    '''
    u = 1 + max([x.key for x in A])  #O(n) find the maximum key
    D = [0] * u                      #O(u) init Direct Access Array
    
    for x in A:                      #O(n) count occurrences
        D[x.key] += 1
    
    for i in range(1,u):             #O(u) cumulative sums
        D[i] += D[i - 1]
    
    for x in list(reversed(A)):      #O(n) reorder the items at A, NOTE: WE ARE REVERSING THE GIVEN A TO MAKE THE SORT STABLE
        A[D[x.key] - 1] = x
        D[x.key] -= 1
    
    return A

class Item:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    def __str__(self) -> str:
        return f"({self.key}, {self.value})"
    
        
my_list = [Item(random.randint(0, 100), f"Value {i+1}") for i in range(20)]
for item in my_list:
    print(item)

print("\n================== COUNTING SORT V1 =================================\n")
for item in counting_sort(my_list):
    print(item)
    
print("\n================== COUNTING SORT V2 =================================\n")
for item in counting_sort_cumulative(my_list):
    print(item)
    

    