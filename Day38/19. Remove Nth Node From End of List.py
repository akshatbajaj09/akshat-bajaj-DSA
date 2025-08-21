# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        l = 0
        while curr != None:
            curr = curr.next
            l += 1
        if l == 1:
            return None
        remove_from_first = l - n + 1
        curr = head
        if remove_from_first < 2:
            head = head.next
        for i in range(remove_from_first - 2):
            # As we need to iterate current to a position before the element to be removed.
            curr = curr.next
        # Now link the curr to curr.next.next:
        curr.next = curr.next.next
        return head
