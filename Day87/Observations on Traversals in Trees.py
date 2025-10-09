# You may have noticed that in the case of Inorder Traversal for traversing to
# the leftmost node, a while loop was used like this:
# while curr or st:
#     while curr:
#         st.append(curr)
#         curr = curr.left
#     ----- Other code ----

# But in case of Postorder Traversal an if block was used to traverse the
# curr pointer to the leftmost node like this:
# while curr or st:
#     if curr:
#         st.append(curr)
#         curr = curr.left
#     ----- Other code ----

# Now why is this difference arising?
# The answer to this lies in the basic need of the order, in the case of inorder
# traversal, the needed flow is LEFT -> ROOT -> RIGHT and in the case of postorder
# it is LEFT -> RIGHT -> ROOT, meaning in inorder DON'T NEED to process the right
# child of the root before processing the root, and hence it is safe to traverse
# to the leftmost child directly via a while loop, but in the case of postorder we
# DO NEED to process the right child of the root before processing the root and hence
# we need to make a conditional check that whether the current root can be processed or
# do we need to process its right child first, which demands a if block rather than
# directly traversing to the left-most child.

# Ok but now can't we process the right-child of the root by popping back to it using
# the entries we are maintaining in stack, since we are appending each root to the
# stack so we can access the root from there and then process its right child right?

# And the answer to this is the destructive nature of the st.pop() command, meaning
# whenever we will try to go back to the root after we are done its left-child, we will
# do curr = st.pop(), setting the curr pointer to the root and then we can work on the
# right child via curr.right, but now we have lost the root, since st.pop() works
# destructively, we can not go back to the root, and that was the exact requirement
# in postorder's flow of LEFT -> RIGHT -> ROOT, hence using the concept of peek node
# via peek = st[-1] and checking at every step using an if-block is needed.
