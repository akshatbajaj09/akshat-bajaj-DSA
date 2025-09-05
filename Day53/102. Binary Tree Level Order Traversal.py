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
        q = deque()
        q.append(root)
        while q:
            same_level = []
            for i in range(len(q)):
                curr = q.popleft()
                same_level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(same_level)
        return ans
