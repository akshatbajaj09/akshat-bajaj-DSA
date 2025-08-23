# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Method - 1 (Two pointers):

    def deleteDuplicates(self, head):
        fake = ListNode(-1, head)
        curr, prev = head, fake
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next

        return fake.next

    # Method - 2 (Using Hashmap):

    def deleteDuplicates2(self, head):
        freq = {}
        curr = head
        while curr:
            if curr.val not in freq:
                freq[curr.val] = 1
            else:
                freq[curr.val] += 1
            curr = curr.next
        dummy = ListNode()
        ans = dummy
        for key, val in freq.items():
            if val > 1:
                continue
            else:
                ans.next = ListNode(key)
                ans = ans.next
        return dummy.next
