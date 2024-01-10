import random


class DirectAccessArray:
    '''
    DirectAccessArray is one of the implementations for the Set Interface
    Direct Access Array is the same as regular array but indices = key,
    which means if key 9 digit long number, then (10^9) different memory locations needed each of which is w-bit long.
    E.g. if w = 64 bits, then (10^9)*64 = Approx. 8GB space for this array. So bad and wasteful!!!
    
    n<<u, n is input size, u is size of DAA for n inputs
    set operations(find(k), insert(x), delete(k)) -> O(1)
    build, order operations -> O(u), so wasteful!
    '''
    def __init__(self, u): self.A = [None] * u
    def __str__(self) -> str:
        return str(self.A)
    def __iter__(self):
        yield from self.A
    def find(self, k): return self.A[k]
    def insert(self, x): self.A[x.k] = x
    def delete(self, k): self.A[k] = None
    def find_next(self, k):
        for i in range(k, len(self.A)):
            if self.A[i] is not None:
                return self.A[i]
    def find_prev(self, k):
        for i in range(k, -1, -1):
            if self.A[i] is not None:
                return self.A[i]
    def find_max(self):
        for i in range(len(self.A)-1, -1, -1):
            if self.A[i] is not None:
                return self.A[i]
    def find_min(self):
        for i in range(len(self.A)):
            if self.A[i] is not None:
                return self.A[i]
    def delete_max(self):
        for i in range(len(self.A)-1, -1, -1):
            x = self.A[i]
            if self.A[i] is not None:
                self.A[i] = None
                return x


# #TEST
# daa = DirectAccessArray(100)
# random_numbers = [random.randint(1, 100) for _ in range(10)]

# for i in random_numbers:
#     daa.insert(i)

# print(daa)