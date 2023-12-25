import random
'''
Task is to implement Set interface from Sequence interface. 
'''
class Array_Seq:
    
    '''
    This is a static array sequence where access is O(1) but insertion and deletion of an element is O(n)
    '''
    
    def __init__(self) -> None:
        self.A = []
        self.size = 0
 
    def __len__(self): return self.size
    def __iter__(self): yield from self.A
    
    def __str__(self) -> str:
        return str(self.A)
    
    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)
        
    def get_at(self, i): return self.A[i]
    def set_at(self, i, x): self.A[i] = x
    
    
    def _copy_forward(self, i, n, A, j):
        #populate array A starting from its j'th index with n elements starting from self.A's i'th element
        for k in range(n):
            A[j + k] = self.A[i + k]
   
    def _copy_backward(self, i, n, A, j):
        for k in range(n-1, -1, -1):
            A[j + k] = self.A[i + k]
    
    def insert_at(self, i, x):
        n = len(self)
        #new list of (n + 1) elements
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)
    
    def delete_at(self, i):
        n = len(self)
        #new list of (n - 1) elements
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x
    
    def insert_first(self, x): self.insert_at(0, x)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_first(self): return self.delete_at(0)
    def delete_last(self): return self.delete_at(len(self) - 1)
 
class Set_Element:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        
    def __str__(self) -> str:
        return str(self.value)
    
    
        
def set_from_sequence(seq):
    '''
    This function creates Set interface from the given Sequence
    '''
    class Set_From_Sequence:
        def __init__(self): self.S = seq()
        def __len__(self): return len(self.S)
        def __iter__(self): yield from self.S
        
        def build(self, X):
            self.S.build(X)
        
        def find(self, k):
            for x in self.S:
                if x.key == k:
                    return x
            return None
        
        def insert(self, x):
            for x in self.S:
                if x.key == x.key:
                    x = x
                    return
            self.S.insert_last(x)
        
        def delete(self,k):
            for i in range(len(self)):
                if self.S.get_at(i).key == k:
                    return self.S.delete_at(i)
        
        def find_min(self):
            min = None
            for x in self.S:
                if min is None or x.key < min.key:
                    min = x
            return min
        
        def find_max(self):
            max = None
            for x in self.S:
                if max is None or x.key > max.key:
                    max = x
            return max
        
        def find_next(self, k):
            min = None
            for x in self.S:
                if x.key > k:
                    if min is None or min.key > x.key:
                        min = x
            return min
                        
        def find_prev(self, k):
            max = None
            for x in self.S:
                if x.key < k:
                    if max is None or max.key < x.key:
                        max = x
            return max
        
        def iter_ord(self):
            x = self.find_min()
            while x:
                yield x
                x = self.find_next(x.key)

    return Set_From_Sequence()




#TEST
sample_elements = [
    Set_Element(0, "InShaAllah"),
    Set_Element(1, "I"),
    Set_Element(2, "study"),
    Set_Element(3, "at"),
    Set_Element(4, "ETH"),
    Set_Element(5, "Zurich"),
    ] 

random.shuffle(sample_elements)
set = set_from_sequence(Array_Seq)
print("Size:", len(set))
set.build(sample_elements)
print("\n\nShuffled elements: \n")
for i in set:
    print(i)
print("\nSize:", len(set))
print("\nPrev of k=5", set.find_prev(5))
print("\nNext of k=4", set.find_next(4))
print("\nSorted elements: \n")
for i in set.iter_ord():
    print(i)
