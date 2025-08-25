# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        for i in range(left - 1):
            prev = curr
            curr = curr.next
        req_p = prev
        req_c = curr  # Will be used to change the links.
        # Reversing the links from left to right:
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Changing remaining links:
        req_p.next = prev
        req_c.next = curr

        return dummy.next
