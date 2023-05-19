def middleNode(linkedList):
    # Write your code here.
    cur = linkedList
    mid = linkedList
    i = 0
    while cur.next is not None:
        i += 1
        cur = cur.next
        if i % 2 == 1:
            mid = mid.next

    return mid


def middleNode_opt(linkedList):
    # Write your code here.
    fast = linkedList
    slow = linkedList
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow
