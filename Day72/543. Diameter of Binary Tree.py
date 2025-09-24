# Approach: The diameter of the binary tree is the maximum among the sums of the
# left subtree's height and right subtree's height of the nodes in the tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.height(root)
        return self.diameter


# The previous solution (which was incorrect):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        # left:
        p1, e1 = root, 0
        while p1.left:
            e1 += 1
            p1 = p1.left
            if not p1.left:
                if p1.right:
                    e1 += 1
                    p1 = p1.right

        # right:
        p2, e2 = root, 0
        while p2.right:
            e2 += 1
            p2 = p2.right
            if not p2.right:
                if p2.left:
                    e2 += 1
                    p2 = p2.left

        return e1 + e2


# This didn't work as in this the assumption was that the diameter or the longest path
# will be between the leftmost and the rightmost node which fails and the debugging of
# if not p1.left:
#   if p1.right:
#       e1 += 1
#       p1 = p1.right
# or this too:
# if not p2.right:
#     if p2.left:
#         e2 += 1
#         p2 = p2.left
# was just hit and trial but still it failed at many cases meaning the approach was wrong.
