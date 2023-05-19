def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    cur = linkedList
    while cur.next is not None:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return linkedList
