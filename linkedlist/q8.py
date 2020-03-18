def loop_detection(ll):
    slow = ll.head
    fast = ll.head

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    
    if fast.next == None or fast.next.next == None:
        return False
    
    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return fast