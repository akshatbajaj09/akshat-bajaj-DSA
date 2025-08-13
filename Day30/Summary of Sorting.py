# Summary of different sorting approaches:

# Bubble sort:
# Largest element gets shifted to the right, just like the larger bubbles
# comes to the surface of water before the smaller ones.
# The approach follows swapping with adjacent elements.
# We can optimize it using a flag for swap.
# Time complexity: O(n^2)
# Space complexity: O(1)

# Insertion sort:
# It considers that the first element is already sorted and hence starts from the
# second element and traverses along the array.
# At every step the encountered number is inserted at its correct position and
# the elements larger than it are shifted one step rightwards.
# Time complexity: O(n^2)
# Space complexity: O(1)

# Selection sort:
# In this in every iteration the smallest element after the current element
# is chosen and swapped with the current element.
# Since, we select our desired element hence the name of selection sort.
# Time complexity: O(n^2)
# Space complexity: O(1)

# Merge Sort:
# It works on the divide and conquer approach via recursion.
# We keep on dividing the array until we have only 1 element left at the end
# of the recursion tree.
# Then these single elements at the end of the tree are compared and sorted
# and then merged via another helper function, collectively making the main
# array sorted when we reach back towards the top of the recursion tree.
# Time complexity: O(nlogn)
# Space complexity: O(n)

# Quick sort:
# This also works on the divide and conquer approach via recursion.
# In this we algorithm we choose a reference point, say p.
# Now all the elements smaller than p are shifted to the left of p and
# the ones larger than it are shifted to the right of it, while p stays in the
# middle of them.
# Time complexity: O(n^2) with an average time complexity of O(nlogn).
# Space complexity: O(1)
