from linked_list import *

def reorder_students(L:Linked_List_Seq):
    n = len(L) // 2
    a = L.head
    for _ in range(n - 1):
        a = a.next
    b = a.next
    x_p, x = a, b
    for _ in range(n):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n
    c = x_p
    a.next = c
    b.next = None
    
    return



def reverse_students(L:Linked_List_Seq):
    n = len(L)
    a = L.head
    b = a.next
    x_p, x = a, b
    for _ in range(n - 1):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n
    L.head = x_p
    a.next = None
    
    return


#TEST
sample_list = [1,2,3,4,5,6,7,8,9,10,11,12]
l = Linked_List_Seq()
l.build(sample_list)
print("\n", l)
reorder_students(l)
print("\n", l)


