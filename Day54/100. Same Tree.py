# Method - 1 (Using helper function):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):

        def same(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and same(left.left, right.left) and same(left.right, right.right)

        return same(p, q)


# Method - 2 (Without using helper function):


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
