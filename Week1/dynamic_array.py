import random

class Dynamic_Array_Seq:
    def __init__(self, r = 2):
        self.A = []
        self.size = 0
        self.r = r
        self._update_bounds()
        self._resize(0)
        
    def __len__(self):
        return self.size
    
    def __str__(self) -> str:
        return str(self.A)
    
    def build(self, X):
        for a in X:
            self.insert_last(a)
            
    def get_at(self, i):
        return self.A[i]
    
    def set_at(self, i, x):
        self.A[i] = x
    
    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]
            
    def _copy_backward(self, i, n, A, j):
        for k in range(n-1, -1, -1):
            A[j + k] = self.A[i + k]
            
    def _update_bounds(self):
        self.upper_size = len(self.A)
        self.lower_size = len(self.A) // (self.r * self.r)
        print("Upper bound size:", self.upper_size)
        print("Lower bound size:", self.lower_size)
    
    def __iter__(self):
        yield from self.A
     
       
    def _resize(self, n):
        '''
        If n//4 < size < n holds, then there is enough space for insertion and no need to allocate a new array.
        
        if n//4 < size < n does not hold, then allocates a new array of bigger size,
        copies forward all existing elements to the new array,
        and updates the existing array to that new array.
        
        NOTE: len(self) and self.size = # elements in the array
              len(self.A) = size of the array
        '''
        if self.lower_size < n < self.upper_size:
            return
        m = max(n,1) * self.r  #at least 1 * self.r space is allocated
        new_A = [None] * m
        self._copy_forward(0, self.size, new_A, 0)
        self.A = new_A
        self._update_bounds()
        
    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1
    
    def delete_last(self):
        x = self.A[self.size - 1]
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)
        return x
    
    def insert_at(self, i, x):
        self.insert_last(None)
        self._copy_backward(i, self.size - i - 1, self.A, i + 1)
        self.A[i] = x
        
    def delete_at(self, i):
        print("delete at index =", i)
        x = self.A[i]
        self._copy_forward(i + 1, self.size - i - 1, self.A, i)
        self.delete_last()
        return x
    
    def insert_first(self, x):
        self.insert_at(0, x)
    
    def delete_first(self):
        return self.delete_at(0)
    
    
    
#TEST (observe how the size of the array is changing with respect to the number of elements)
random_numbers = [random.randint(1, 100) for _ in range(10)]

dynamic_ar = Dynamic_Array_Seq()
print(dynamic_ar)

# keep inserting_last 10 random elements
print("================== INSERTING 10 RANDOM NUMBERS... =======================")
for i in random_numbers:
    dynamic_ar.insert_last(i)
    print(dynamic_ar)

print("================== AND NOW DELETING... =======================")
#keep deleting those 10 elements
for i in range(len(dynamic_ar)-1, -1, -1):
    dynamic_ar.delete_at(i)
    print(dynamic_ar)





# for i in random_numbers:
#     dynamic_ar.insert_last(i)
#     print(dynamic_ar)

# dynamic_ar.insert_last(2)
# dynamic_ar.insert_first(56)
# dynamic_ar.insert_last(3)
# print(dynamic_ar)

# for i in dynamic_ar:
#     print(i)

# dynamic_ar.delete_at(2)
# print(dynamic_ar)

# dynamic_ar.delete_last()
# print(dynamic_ar)

# dynamic_ar.delete_first()
# print(dynamic_ar)
    

        
    
        
        
        