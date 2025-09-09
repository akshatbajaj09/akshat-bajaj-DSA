# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def valid(self, root, mn, mx):
        if not root:
            return True  # A null tree is considered a valid BST.
        if not (mn < root.val < mx):
            return False
        checkLeft = self.valid(root.left, mn, root.val)
        checkRight = self.valid(root.right, root.val, mx)
        return checkLeft and checkRight

    def isValidBST(self, root):
        # return self.valid(root, -(2**31), 2**31) -> fails because
        # -(2**31) and 2**31 are not included.
        # return self.valid(root, -(2**31) - 1, 2**31 + 1)  # passes as
        # now -(2**31) and 2**31 are included as well.
        # But we also have another way to do it:
        return self.valid(root, float("-inf"), float("inf"))
        # float("-inf") gives a number smaller than any real number and
        # float("inf") gives a number larger than any real number.
