class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None
        self.prev = None

    # traversing to the i-th Node
    def later_node(self, i):
        if i == 0: 
            return self
        assert self.next  #check if the next reference is not None
        return self.next.later_node(i - 1)
    
    def prev_node(self, i):
        if i == 0:
            return self
        assert self.prev 
        return self.prev.prev_node(i - 1)


class Doubly_Linked_List_Seq:
    '''
    Getting/Setting: O(n), since we have to follow the next nodes of each element till we reach the i-th element
    Insertion/Deletion at the beginning: O(1), we just relink the head
    Insertion/Deletion at the i-th position: O(n), since we have to traverse till the i-th position
    Insertion/Deletion at the end: O(n): this can be optimized to O(1) if we keep track of additional "tail" property 
    '''
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        #self.size = 0
    
    
    
    # def __len__(self):
    #     return self.size
    
    def __iter__(self):
        node = self.head
        while node:  #while node is not None
            yield node.item
            node = node.next
            
            
    def __str__(self) -> str:
        res = ''
        for i in self:
            res = res +" " + str(i)
        return res
            
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
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = x
            self.tail = x
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete_first(self):
        assert self.head
        x = self.head.item
        self.head = self.head.next 
        if self.head is None: self.tail = None #empty list
        else: self.head.prev = None
        return x
    
    
    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Doubly_Linked_List_Node(x)
        node = self.head.later_node(i-1)
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        new_node.prev = node
        
    def delete_at(self, i):
        if i == 0:
            self.delete_first()
            return
        node = self.head.later_node(i-1)
        x = node.next.item
        node.next = node.next.next
        node.next.prev = node
        return x
    
    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.tail is None:
            self.head = x
            self.tail = x
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    
    def delete_last(self):
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None: self.head = None
        else: self.tail.next = None
        return x
    
    def remove_nodes_between(self, x1, x2):
        if x1 == self.head: self.head = x2.next
        else: x1.prev.next = x2.next
        if x2 == self.tail: self.tail = x1.prev
        else: x2.next.prev = x1.prev
        return Doubly_Linked_List_Seq(x1, x2)
        
    def splice_L(self, x, L):
        xn = x.next
        x.next = L.head
        L.head.prev = x
        L.tail.next = xn
        if xn: xn.prev = L.tail
        else: self.tail = L.tail
        L = None
        

# array = ['I', 'Love', 'ETH', 'Zurich.', 'InShaAllah', 'Soon', 'I', 'Will', 'Be', 'There...']
# linked = Linked_List_Seq()
# linked.build(array)
# print(linked.size)
# print(linked.head.item)
# for i in linked:
#     print(i)
# linked.insert_last('And Do A Great Job!')
# print(linked)
# linked.delete_at(3)
# print(linked)
# linked.set_at(2, 'ETH Zurich')
# print(linked)
# print(linked.get_at(7))
# linked.insert_first('I am Bekhruz')
# print(linked)
# linked.insert_at(1, 'I am a CS student')
# print(linked)
# linked.delete_first()
# print(linked)
# linked.insert_last("Something")
# print(linked)
# print("Deleted item", linked.delete_last())
# print(linked)


