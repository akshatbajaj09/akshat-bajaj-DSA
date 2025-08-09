# Just comments file to supplement learning:

# Observation for the problems:

# 283. Move Zeroes → push all zeroes to the right.
# 27. Remove Element → push all target elements to the right.
# 26. Remove Duplicates from Sorted Array → push duplicates to the right.
# 80. Remove Duplicates from Sorted Array II → push excess duplicates to the right.
# 905. Sort Array By Parity → push odd numbers to the right.

# Observation:

# All of these problems can be done using a 2 pointer approach in which we:
# 1. Maintain a left pointer for the position to place the next “wanted” element.
# 2. Iterate with a right pointer through the array.
# 3. If nums[right] is wanted (matches the condition of the wanted elements),
# swap nums[left] and nums[right], then increment left.
# 4. At the end, elements before left are the valid/wanted ones,
# and the unwanted ones are shifted to the right.

# Pseudocode:

# left = 0
# for right in range(len(nums)):
#     if condition(nums[right]):  # wanted element
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
# return left  # or nums if no length needed

# Analysis:

# This approach works in-place, O(n) time, and keeps the
# relative order of the wanted elements.
