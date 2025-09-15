# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        queue = deque()
        queue.append(root)
        while queue:
            curr_level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_level)
        return ans
