import random

class Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    # traversing to the i-th Node
    def later_node(self, i):
        if i == 0: 
            return self
        assert self.next  #check if the next reference is not None
        return self.next.later_node(i - 1)


class Linked_List_Seq:
    '''
    Getting/Setting: O(n), since we have to follow the next nodes of each element till we reach the i-th element
    Insertion/Deletion at the beginning: O(1), we just relink the head
    Insertion/Deletion at the i-th position: O(n), since we have to traverse till the i-th position
    Insertion/Deletion at the end: O(n): this can be optimized to O(1) if we keep track of additional "tail" property 
    '''
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        node = self.head
        while node:  #while node is not None
            yield node.item
            node = node.next
   
            
    def build(self,X):
        for a in reversed(X):
            self.insert_first(a)
    
    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item
    
    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x
        
    def insert_first(self, x):
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete_first(self):
        x = self.head.item
        self.head = self.head.next 
        self.size -= 1
        return x
    
    
    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i-1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1
        
    def delete_at(self, i):
        if i == 0:
            self.delete_first()
            return
        node = self.head.later_node(i-1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x
    
    def insert_last(self, x):
        self.insert_at(len(self), x)
    
    def delete_last(self):
        return self.delete_at(len(self) - 1)
        
        
        
def set_from_sequence(seq):
    '''
    This function creates Set interface from the given Sequence
    '''
    class Set_From_Sequence:
        def __init__(self): self.S = seq()
        def __len__(self): return len(self.S)
        def __iter__(self): 
            for x in self.S:
                yield x
        
        def __str__(self) -> str:
            res = ''
            for i in self:
                res = res +" " + str(i)
            return "[" + res + "]"
        
        def build(self, X):
            self.S.build(X)
        
        def find(self, k):
            for x in self.S:
                if x.key == k:
                    return x
            return None
        
        def insert(self, x):
            for e in self.S:
                if e.key == x.key:
                    e = x
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

    return Set_From_Sequence




class HashTableSet:
    '''
    Used Universal Family of Hash Functions
    
    Collisions are solved with Chaining
    
    Chains are implemented with LinkedList that supports dynamic set operations
    
    Time Complexities:
    build(X): O(n)e, expected linear 
    find(k): O(1)e, expected constant time
    insert/delete(x): O(1)ae, amortized expected constant time
    find_min/max(): O(n), linear
    find_next/prev(k): O(n), linear
    '''
    def __init__(self, r = 2):
        self.chain_set = set_from_sequence(Linked_List_Seq)
        self.A = []
        self.size = 0
        self.r = r            # fill ratio
        self.p = 2**31 - 1    # the largest prime that can fit in 32-bit word
        self.a = random.randint(1, self.p-1)
        self._compute_bounds()
        self._resize(0)
        
    def __len__(self): return self.size # #items stored
    
    def __iter__(self):
        for X in self.A:
            yield from X
    
    def print_items(self):
        for i in range(len(self.A)):
            print(len(self.A[i]),"sized chain items at Hash", i, ":", [x.value for x in self.A[i]])

            
    def get_table_size(self):
        return len(self.A)
    
    def build(self, X):             # O(n)e = expected linear!
        for x in X: self.insert(x)
        
    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m
    
    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // self.r * self.r
        
    def _resize(self, new_requested):
        if (new_requested<=self.lower) or (self.upper<=new_requested):
            m = max(new_requested, 1) * self.r
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                hash = self._hash(x.key, m)
                A[hash].insert(x)
            self.A = A
            self._compute_bounds()
            
    def find(self, k):                         # O(1)e
        hash = self._hash(k, len(self.A))
        return self.A[hash].find(k)
    
    def insert(self, x):                       # O(1)ae
        self._resize(self.size + 1)
        hash = self._hash(x.key, len(self.A))
        self.A[hash].insert(x)
        self.size += 1
        
    def delete(self, k):                       # O(1)ae
        hash = self._hash(k, len(self.A))
        x = self.A[hash].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x
    def find_min(self): # O(n)
        out = None
        for x in self:
            if out is None or x.key < out.key:
                out = x
        return out
    def find_max(self): # O(n)
        out = None
        for x in self:
            if out is None or x.key > out.key:
                out = x
        return out
    
    def find_next(self, k): # O(n)
        out = None
        for x in self:
            if x.key > k:
                if out is None or out.key > x.key:
                    out = x
        return out
    def find_prev(self, k): # O(n)
        out = None
        for x in self:
            if x.key < k:
                if out is None or out.key < x.key:
                    out = x
        return out
    
    def iter_order(self):   # O(n^2)
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)


class Set_Element:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        
    def __str__(self) -> str:
        return str(self.value)
    

#TEST
sample_elements = [
    Set_Element(6, "InShaAllah"),
    Set_Element(1, "I"),
    Set_Element(2, "study"),
    Set_Element(3, "at"),
    Set_Element(4, "ETH"),
    Set_Element(5, "Zurich"),
    ] 

hash_table = HashTableSet()
hash_table.build(sample_elements)
print("\n DISPLAY HASH TABLE")
hash_table.print_items()
print("\n ITER ORDER")
for i in hash_table.iter_order():
    print(i)
print("\n FIND ITEM WITH MIN KEY")
print(hash_table.find_min())
print("\n FIND ITEM WITH MAX KEY")
print(hash_table.find_max())
print("\n FIND ITEM AFTER THE ITEM WITH KEY 4")
print(hash_table.find_next(4))
print("\n FIND ITEM BEFORE THE ITEM WITH KEY 4")
print(hash_table.find_prev(4))
print("\n INSERT ITEM WITH KEY 10 AND VALUE 'THE'")
item = Set_Element(10, "THE")
hash_table.insert(item)
print("\n DISPLAY HASH TABLE")
hash_table.print_items()
print("\n FIND ITEM WITH KEY 10")
print(hash_table.find(10))   
print("\n DELETE ITEM WITH KEY 10")
hash_table.delete(10)
print("\n DISPLAY HASH TABLE")
hash_table.print_items()
     
        
        
        