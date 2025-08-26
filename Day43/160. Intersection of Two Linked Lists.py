# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        l1 = 1
        curr = headA
        while curr.next:
            l1 += 1
            curr = curr.next
        l2 = 1
        curr = headB
        while curr.next:
            l2 += 1
            curr = curr.next
        p1, p2 = headA, headB
        if l1 > l2:
            for i in range(l1 - l2):
                p1 = p1.next
            while p1:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next
        else:
            for i in range(l2 - l1):
                p2 = p2.next
            while p1:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next
        return None
