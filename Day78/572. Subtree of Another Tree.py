# Approach:


# Find the inorder traversals of both and if the inorder traversal of subRoot is in the
# inorder traversal of root, then return True.


# Implementation:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Finding the inorder traversal:
    def inorderTraversal(self, root):
        ans = []
        st = []
        curr = root
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

    def isSubtree(self, root, subRoot):
        inorder_root = self.inorderTraversal(root)
        inorder_subroot = self.inorderTraversal(subRoot)
        # Making a list of strings for root and subroot to check if subroot's string is
        # in root or not:
        inorder_root_str_list = []
        for num in inorder_root:
            inorder_root_str_list.append(str(num))

        inorder_subroot_str_list = []
        for num in inorder_subroot:
            inorder_subroot_str_list.append(str(num))
        # Joining the lists:
        inorder_root_str = "".join(inorder_root_str_list)
        inorder_subroot_str = "".join(inorder_subroot_str_list)

        return inorder_subroot_str in inorder_root_str


# The above code is wrong as for cases like:
# root = [10,5,null,4] and subroot = [10,4,null,null,5]
# the inorder traversal will be same: 4,5,10 and the resulting string will be 4510
# for both and hence 4510 in 4510 will return True, meaning the given subRoot is valid
# which is wrong.

# Also now on noticing this case, another possible flaw is let's say the inorder traversal
# for the root is 4,5,1,0 and for subroot is 4,5,10 now both will return 4510 as a string
# which is also missed here, so the above logic of inorder traversal fails.


# Approach - 2:
# Recursive:
# As the question is itself named Subtree of Another Tree meaning we can break
# bigger problems to smaller ones, directly implying recursion.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.same(p.left, q.left) and self.same(p.right, q.right)

    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
