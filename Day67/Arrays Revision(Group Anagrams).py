# Revising arrays:

# Approach - 1:
# Make an array corresponding to the frequency of each alphabet as it stays same for
# anagrams, then make a dict of keys as tuple of these arrays and values as corresponding
# strings.
# Then make a list of ans while grouping the values having same keys and
# making another group for new keys.

# Implementation:


class Solution:
    def groupAnagrams(self, strs):
        my_dict = {}
        ans = []
        for key in my_dict:
            if not ans:
                ans.append([key])
                continue
            print(key, ans[-1][0])
            if my_dict[key] == my_dict[ans[-1][0]]:
                ans[-1].append(key)
            else:
                ans.append([key])
        return ans


# The above implementation is wrong as it only compares the current word with
# the last group.


# Better and corrected approach:
class Solution:
    def groupAnagrams(self, strs):
        my_dict = {}
        for i in range(len(strs)):
            array = [0] * 26
            for j in range(len(strs[i])):
                char = strs[i][j]
                array_ind = ord(char) - ord("a")
                array[array_ind] += 1
            key = tuple(array)
            if key not in my_dict:
                my_dict[key] = [strs[i]]
            else:
                my_dict[key].append(strs[i])
        return list(my_dict.values())
