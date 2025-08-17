# Just comments file for a new algorithm:

# The Boyer–Moore Majority Vote Algorithm:

# Time complexity: O(n) 
# Space complexity: O(1)

# Core Idea:

# If an element is the majority, it will survive all "pair eliminations"
# against other elements.

# Every time we see the same element as our current candidate → increase count.

# Every time we see a different element → decrease count (cancel them out).

# If the count hits zero → pick the current element as the new candidate.

# At the end, the candidate must be the majority element 
# (since majority > n/2 ensures it can’t be fully canceled).