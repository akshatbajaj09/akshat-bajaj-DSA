# Method - 1:
# Merge sort:
class Solution:
    def divide(self, nums, l, r):
        if l == r:
            return
        else:
            m = (l + r) // 2
            self.divide(nums, l, m)
            self.divide(nums, m + 1, r)
            self.merge(nums, l, m, r)

    def merge(self, nums, l, m, r):
        i, j, k = 0, 0, l
        a = nums[l : m + 1]
        b = nums[m + 1 : r + 1]
        while k <= r:
            if i == len(a):
                nums[k] = b[j]
                j += 1
                k += 1
            elif j == len(b):
                nums[k] = a[i]
                i += 1
                k += 1
            elif a[i] < b[j]:
                nums[k] = a[i]
                i += 1
                k += 1
            else:
                nums[k] = b[j]
                j += 1
                k += 1
        return nums

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.divide(nums, 0, len(nums) - 1)


# Method - 2:
# Using a frequency dictionary:
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_dict = {0: 0, 1: 0, 2: 0}
        for num in nums:
            freq_dict[num] += 1

        i = 0
        while freq_dict[0]:
            nums[i] = 0
            i += 1
            freq_dict[0] -= 1
        while freq_dict[1]:
            nums[i] = 1
            i += 1
            freq_dict[1] -= 1
        while freq_dict[2]:
            nums[i] = 2
            i += 1
            freq_dict[2] -= 1


# Method - 3:
# Dutch flag method:
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # i += 1 -> WRONG! -> Do not increment i here.
