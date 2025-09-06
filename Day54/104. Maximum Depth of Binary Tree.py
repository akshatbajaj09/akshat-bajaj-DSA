# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Method - 1 (Recursion):


class Solution:
    def maxDepth(self, root):
        # Base case:
        if not root:
            return 0
        # Recursive case:
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


# Method - 2 (BFS):


from collections import deque


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        levels = 0
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            levels += 1
        return levels
