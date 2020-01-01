class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def return_k(l, k):
    counter = 0
    a = l
    while a.next:
        counter += 1
        a = a.next
    
    counter += 1
    
    while counter != k:
        l = l.next
        counter -= 1
    return l.val

def return_k_2(l, k):
    """recursive"""
    if not l:
        return 0
    index = return_k_2(l.next, k) + 1
    if index == k:
        print(l.val)
    return index

def return_k_3(l, k):
    """iterative"""
    p1 = l
    p2 = l
    for i in range(k):
        if not p1:
            break
        p1 = p1.next
    
    while p1:
        p1 = p1.next
        p2 = p2.next
    
    return p2.val

if __name__ == '__main__':
    l = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l3 = ListNode(1)
    l4 = ListNode(2)
    l5 = ListNode(1)

    l.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    print(return_k(l,4))
    return_k_2(l,4)
    print(return_k_3(l,2))