# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    # Method - 1 (Hashing):

    def detectCycle(self, head):
        my_set = set()
        curr = head
        while curr:
            if curr in my_set:
                return curr
            else:
                my_set.add(curr)
                curr = curr.next
        return None

    # Method - 2 (Two pointers):

    def detectCycle(self, head):
        slow = head
        fast = head
        hasCycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        if not hasCycle:
            return None
        # Calculating the length of the loop:
        l = 1
        while slow.next != fast:
            slow = slow.next
            l += 1
        # Resetting slow and fast to head:
        slow = head
        fast = head
        # Advancing the fast pointer to l nodes:
        for i in range(l):
            fast = fast.next
        # Now the point of meeting of slow and fast will be the start of cycle:
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    # Method - 3 (Two pointers without needing the length):

    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
