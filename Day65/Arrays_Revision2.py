# Problem:
# Longest common prefix:
# My solution:
class Solution:
    def longestCommonPrefix(self, strs):
        curr_str = strs[0]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if j < len(curr_str) and strs[i][j] == curr_str[j]:
                    continue
                else:
                    prefix = curr_str[:j]
                    break
        return prefix


# But this has 2 main flaws:

# 1. Consider, strs = ["flow", "fl", "flower"] now the program identifies that "fl" is a
# prefix of "flow" but our prefix is not updated to "fl" and always stays the first element
# of strs, and on further execution we check "flower" and "flow" and return flow as
# the ans which is incorrect.

# So, the 1st problem is that we are not updating our prefix.

# 2. Consider, strs = ["a", "ab"] now this program will never hit the else block and the
# prefix will never be defined and hence will throw an error when we try to return it.

# And hence the second problem is when we never hit the else block.

# Corrected code:


# Method - 1:
# Horizontal scanning (One string at a time):
# We start with a guess for the prefix (the first word) and then shorten it as
# we check it against each subsequent word in the list.


class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(1, len(strs)):
            curr_str = strs[i]
            while curr_str[: len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Method - 2:
# Vertical Scanning (One char at a time):
# We look at the first character of every word, then the second character of every word,
# and so on, moving downwards in columns.
# Imagine the words are written one below the other, lined up in columns.
# We put our finger on the first letter of the first word and scan down that column.
# If all the letters in the column are the same, we move our finger to the second column
# and repeat. The moment we find a column where the letters don't all match, we know the
# common prefix is everything we successfully scanned before that point.


class Solution:
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            char_to_check = strs[0]
            for j in range(1, len(strs)):
                if i == len(strs(j)) or strs[j][i] != char_to_check:
                    return strs[0][:i]
        return strs[0]


# Method - 3:
# Sorting (This method sorts the array and then compares only the first and last strings):


class Solution:
    def longestCommonPrefix(self, strs):
        ans = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                return ans
        return ans
