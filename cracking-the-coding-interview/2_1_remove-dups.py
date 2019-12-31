class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# solution 1 
# with extra memory
def remove_dups(l):
    a = ListNode(0)
    dummy = a
    s = set()
    if l.next:
        s.add(l.val)
        a.next = ListNode(l.val)
        a = a.next
    else:
        return l
    while l.next:
        if l.val in s:
            l = l.next
        else:
            s.add(l.val)
            a.next = ListNode(l.val)
            a = a.next
    
    return dummy.next

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


    l = remove_dups(l)

    while l:
        print(l.val)
        l = l.next