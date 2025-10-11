# Method - 1:
# Finding all the levels and then pushing the rightmost element of each level in the ans:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root):
        ans = []
        if not root:
            return ans
        queue = deque()
        queue.append(root)
        while queue:
            curr_level = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_level[-1])
        return ans


# Method - 2:
# Directly adding the rightmost node in the ans, instead of finding all the levels:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root):
        ans = []
        if not root:
            return ans
        queue = deque()
        queue.append(root)
        while queue:
            curr_size = len(queue)
            for i in range(curr_size):
                node = queue.popleft()
                if i == curr_size - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
