# The sorting approach:
# Key idea: All anagrams will be same when sorted.


class Solution:
    def groupAnagrams(self, strs):
        my_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in my_dict:
                my_dict[sorted_word] = [word]
            else:
                my_dict[sorted_word].append(word)
        return list(my_dict.values())


# Revisiting the approach of yesterday:
# Key idea: Every anagram in strs will have the same frequency of each letter.


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


# Comparison between the 2 methods:
# The sorting method is less efficient than the character counting method but
# it offers better readability.
