# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Reversing the second half (using two pointers):
    def reverse(self, slow):
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        return prev

    def isPalindrome(self, head):
        # Handling the edge case:
        if head.next == None:
            return True
        # Finding the second half:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # Reversing the second half:
        newHead = self.reverse(slow)
        # Comparing the first and second half:
        p1 = head
        p2 = newHead
        while p2:
            if p1.val != p2.val:
                # Bring the given input back to the original form:
                self.reverse(newHead)
                return False
            else:
                p1 = p1.next
                p2 = p2.next
        # Bring the given input back to the original form:
        self.reverse(newHead)
        return True
