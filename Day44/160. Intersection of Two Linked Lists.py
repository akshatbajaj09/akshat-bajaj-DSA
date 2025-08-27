# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Method - 1:
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        count = 0
        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if p1 == None:
                p1 = headB
                count += 1
            if p2 == None:
                p2 = headA
            if count > 1:
                return None
        return None  # This return None statement is redundant.

    # As we have a while True loop, the code will never reach the last line
    # and the loop has to be exited from inside.

    # Method - 2 (same logic as Method - 1 but cleaner):
    def getIntersectionNode2(self, headA, headB):
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

    # Method - 3 (Using sets):
    def getIntersectionNode3(self, headA, headB):
        nodesA = set()
        curr = headA
        while curr:
            nodesA.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in nodesA:
                return curr
            else:
                curr = curr.next
        return None
