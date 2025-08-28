# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # Method - 1 (Hashing):

    def hasCycle(self, head):
        my_set = set()
        curr = head
        while curr:
            if curr in my_set:
                return True
            else:
                my_set.add(curr)
                curr = curr.next
        return False

    # Method - 2 (Two - pointers):

    def hasCycle2(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
