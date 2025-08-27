# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Creating a new Linked list for ans:
        ans = ListNode()
        curr = ans
        # Adding:
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)
            # Update pointers:
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            curr = curr.next
        return ans.next
