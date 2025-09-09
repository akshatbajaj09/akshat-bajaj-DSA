# Method - 1 (Brute force approach):


# Say we need to find the 3rd smallest element, so we will find
# the smallest element (1st smallest), delete it and then find
# smallest again (2nd smallest) and delete that too and then
# finally we will return the smallest again (3rd smallest).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSmallest(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        if not root:
            return None
        # Search the node to be deleted:
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
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
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root

    def kthSmallest(self, root, k):
        for i in range(k - 1):
            curr_smallest = self.findSmallest(root)
            root = self.deleteNode(root, curr_smallest.val)
        return (self.findSmallest(root)).val

    # Method - 2 (Using inorder traversal -> Recursively):

    def inorderTraversal(self, root):
        ans = []

        def inorder(root):
            # Base case:
            if not root:
                return
            # Recursive case:
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
            return ans

        return inorder(root)

    def kthSmallest2(self, root, k):
        return (self.inorderTraversal(root))[k - 1]

    # Method - 3 (Using inorder traversal -> Iteratively):

    def inorderTraversal2(self, root):
        ans = []
        st = []
        curr = root
        while curr or st:
            while curr:
                # Go to extreme left:
                st.append(curr)
                curr = curr.left
            # Now we go to the root in our order of left -> root -> right:
            curr = st.pop()
            ans.append(curr.val)
            # Move to the right subtree:
            curr = curr.right
        return ans

    def kthSmallest3(self, root, k):
        return (self.inorderTraversal2(root))[k - 1]

    # Method - 4 (Without finding the complete inorder traversal and saving memory):

    def inorderTraversal3(self, root, k):
        n = 0
        st = []
        curr = root
        while curr or st:
            while curr:
                # Go to extreme left:
                st.append(curr)
                curr = curr.left
            # Now we go to the root in our order of left -> root -> right:
            curr = st.pop()
            n += 1
            if n == k:
                return curr.val
            # Move to the right subtree:
            curr = curr.right

    def kthSmallest4(self, root, k):
        return self.inorderTraversal3(root, k)
