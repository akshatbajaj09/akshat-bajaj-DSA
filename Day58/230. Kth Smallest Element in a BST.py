# Correction in Method - 1 (Brute force approach) from Day57:
# Recap of what we did:
# In the brute force method we searched the smallest element
# and deleted it and then searched the smallest element again and deleted it too and
# we continued this till we found the Kth smallest element.
# Mistake:
# Using the above approach we modified our input data by deleting elements from it which
# isn't a good practice.
# Solution:
# We can insert the deleted elements back again.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSmallest(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root, target):
        if not root:
            return None
        if target < root.val:
            root.left = self.deleteNode(root.left, target)
        elif target > root.val:
            root.right = self.deleteNode(root.right, target)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find min in right subtree:
                curr = root.right
                while curr.left:
                    curr = curr.left
                # Delete the duplicate:
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root

    def insertNode(self, root, key):
        newNode = TreeNode(key)
        if not root:
            return newNode
        curr = root
        if key < curr.val:
            curr.left = self.insertNode(curr.left, key)
        else:
            curr.right = self.insertNode(curr.right, key)
        return root

    def kthSmallest(self, root, k):
        curr_smallest = []
        for i in range(k - 1):
            curr_smallest.append(self.findSmallest(root))
            root = self.deleteNode(root, (curr_smallest[i]).val)
        ans = self.findSmallest(root)
        # Inserting back the deleted nodes:
        for i in range(k - 1):
            root = self.insertNode(root, (curr_smallest[i]).val)
        return ans.val
