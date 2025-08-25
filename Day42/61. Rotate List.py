# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Method - 1 (The Ring Method):

    def rotateRight(self, head, k):
        # Edge cases:
        if (not head) or (not head.next):
            return head
        # Find the tail and length:
        l = 0
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
        l += 1
        # Calculate effective rotations:
        k = k % l
        # Simple case (k was a multiple of l):
        if k == 0:
            return head
        # Rotating:
        curr = head
        for i in range(l - k - 1):
            curr = curr.next
        tail.next = head
        head = curr.next
        curr.next = None
        # Returning the rotated list:
        return head

    # Method - 2 (The Three-Reversal Algorithm):

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def rotateRight(self, head, k):
        # Edge cases:
        if (not head) or (not head.next):
            return head
        # Finding the length and tail:
        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
        # Find the effective rotations:
        k = k % l
        # Handle the simple case:
        if k == 0:
            return head
        # Splitting the linked list about kth node:
        curr = head
        for i in range(l - k - 1):
            curr = curr.next
        second_half = curr.next
        curr.next = None
        first_half = head
        # Reverse the first half:
        rev_first_half = self.reverse(first_half)
        # Reverse the second half:
        rev_second_half = self.reverse(second_half)
        # Connect the splitted parts after reversing them:
        first_half.next = rev_second_half
        head = rev_first_half
        # Reverse the connected list again:
        ans = self.reverse(head)
        # Return the rotated list:
        return ans
