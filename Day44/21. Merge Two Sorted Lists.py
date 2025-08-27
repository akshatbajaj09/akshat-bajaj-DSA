# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # Edge case (if both lists are empty):
        if (not list1) and (not list2):
            return None
        # Now at least one list is non-empty:
        dummy = ListNode()
        curr = dummy
        p1, p2 = list1, list2
        while True:
            while not p1:
                curr.next = p2
                return dummy.next
            while not p2:
                curr.next = p1
                return dummy.next
            # Comparing the values:
            if p1.val < p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
            curr = curr.next
