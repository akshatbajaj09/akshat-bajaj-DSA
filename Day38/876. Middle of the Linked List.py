# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        curr = head
        l = 0
        while curr != None:
            curr = curr.next
            l += 1

        curr = head
        for i in range(l // 2):
            curr = curr.next

        return curr

    # Method - 2 (Concept of fast and slow pointers):

    def middleNode2(self, head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
