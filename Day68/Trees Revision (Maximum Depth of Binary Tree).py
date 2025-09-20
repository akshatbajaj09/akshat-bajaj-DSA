# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if not root:
            return 0
        left = 1 + self.depth(root.left)
        right = 1 + self.depth(root.right)
        return max(left, right)

    def maxDepth(self, root):
        return self.depth(root)


# Earlier we did it using level order traversal (BFS), and now we used the DFS approach
# using recursion.
