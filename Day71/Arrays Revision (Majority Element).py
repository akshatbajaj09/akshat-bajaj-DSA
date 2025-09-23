# Method - 1 (Brute force):
# Approach - Iterate through each element and count its occurence using the
# in-built count method and then return the num if the count is greater than n / 2.


class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        for num in nums:
            if nums.count(num) > n / 2:
                return num


# The above method gives TLE.


# Method - 2 (Sorting):
# Approach - After sorting the middle element will be the majority element.


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


# Method - 3 (Using a hashmap):
# Approach - Count the occurences of each element and store them in a hashmap then
# return the key with the value > n / 2.


class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        for key, val in freq_dict.items():
            if val > n / 2:
                return key
