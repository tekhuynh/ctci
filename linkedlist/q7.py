def is_intersecting(l1, l2):
    last1 = l1.head
    last2 = l2.head

    while last1.next != None:
        last1 = last1.next
    while last2.next != None:
        last2 = last2.next
    
    return last1 is last2