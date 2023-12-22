'''
Week: 1 
Recitation: 2 
Problem: 1

Problem definition:
Suppose the next pointer of the last node of a linked list points to an earlier node in the list, 
creating a cycle. Given a pointer to the head of the list (without knowing its size), describe a 
linear-time algorithm to find the number of nodes in the cycle. Can you do this while using 
only constant additional space outside of the original linked list? 

Solution is given in the build_cycle() and get_cycle_size() methods below.
Implementation of get_cycle_size() is called Floyd’s Cycle-Finding Algorithm

'''


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
    def __str__(self) -> str:
        res = ''
        for i in self:
            res = res +" " + i
        return res
            
    def build(self,X):
        for a in reversed(X):
            self.insert_first(a)
            
    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item
    
    def insert_first(self, x):
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def build_cycle(self, cycle_start_index):
        '''
        Links the last node of the linked list to the node at cycle_start_index, forming a cycle within the linked list
        '''
        cycle_start_node = self.head.later_node(cycle_start_index)
        self.head.later_node(self.size - 1).next = cycle_start_node
    
    def get_cycle_size(self):
        '''
        Check if there is a cycle in the linked list. If yes, then count the size using the inner loop, else return 0
        Time complexity: O(n), since each node is visited at most twice: 1st is checking if there is a cycle 
        and 2nd is computing the length of the cycle
        '''
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #there is a cycle!
                 fast = fast.next
                 counter = 1 #since we have initially set fast_pointer = fast_pointer.next on above line
                 while fast != slow:
                     counter += 1
                     fast = fast.next
                 return counter
        return 0
    

        
            
   

array = ['I', 'Love', 'ETH', 'Zurich.', 'InShaAllah', 'Soon', 'I', 'Will', 'Be', 'There...']
linked = Linked_List_Seq()
linked.build(array)
linked.build_cycle(4) #builds a cycle from 'InShaAllah'
print("Number of items in the cycle: ", linked.get_cycle_size())
