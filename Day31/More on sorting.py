# The sorting algorithms can have various classifications, like:

# On the basis of stability:
# Stable vs Unstable:

# If the order of the same elements remain intact then the algorithm is said to be
# stable, otherwise it is unstable. Example:
# nums = [5(first, say 5a), 1, 2, 5(second, say 5b), 3]
# If after sorting the output is like this:
# nums = [1, 2, 3, 5a, 5b] then the algorithm is stable since the order of the same
# element (5) remains intact, otherwise if after sorting the output was:
# nums = [1, 2, 3, 5b, 5a] then the algorithm is unstable.

# On the basis of adaptability:
# Adaptive vs Non-adaptive:

# If an algorithm adapts to give more efficiency in terms of time and space
# complexity, depending on the condition of the given array then it is said to
# be adaptive. Like if the given array is already sorted or has only 1 unsorted
# element then if our algorithm adapts to give better efficiency then it is
# adaptive. Otherwise if the algorithm maintains an approximately same time
# and space complexity irrespective of the condition of the given array, then the
# algorithm is said to be Non-adaptive.

# On the basis of memory allocation:
# In-place vs Non in-place:

# If our sorting algorithm does not use any extra space and has a constant
# space complexity then the given sorting algorithm fits in the category of
# in-place sorting algorithms. But, if our algorithm does not possess a
# constant space complexity then it is a Non in-place sorting algorithm.
