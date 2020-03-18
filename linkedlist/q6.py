def palindrome(ll):
    node = ll.head
    items = []
    while node != None:
        items.append(node.val)
        node = node.next
    
    num_items = len(items)
    for i in range(int(num_items/2)):
        if item[i] != item[num_items-1-i]:
            return False
    return True

