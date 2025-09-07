# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Method - 1 (Using loops):
    def insertIntoBST(self, root, val: int):
        newNode = TreeNode(val)
        if not root:
            return newNode
        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = newNode
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = newNode
                    break
                else:
                    curr = curr.right
        return root

    # Method - 2 (Recursive approach):
    def insertIntoBST2(self, root, val: int):
        newNode = TreeNode(val)
        if not root:
            return newNode
        curr = root
        if val < curr.val:
            curr.left = self.insertIntoBST2(curr.left, val)
        else:
            curr.right = self.insertIntoBST2(curr.right, val)
        return root
