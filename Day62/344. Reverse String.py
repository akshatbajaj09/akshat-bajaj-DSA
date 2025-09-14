class Solution:
    def helper(self, s, l, r):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        self.helper(s, l + 1, r - 1)

    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s) - 1)
