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


# The above solution is incorrect and will be worked on later.
