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
    
    
static_ar = Array_Seq()

static_ar.insert_first(1)
static_ar.insert_last(0)
print(static_ar)

static_ar.insert_first(2)
static_ar.insert_last(3)
print(static_ar)

for i in static_ar:
    print(i)

static_ar.delete_at(2)
print(static_ar)

static_ar.delete_last()
print(static_ar)

static_ar.delete_first()
print(static_ar)
    

    