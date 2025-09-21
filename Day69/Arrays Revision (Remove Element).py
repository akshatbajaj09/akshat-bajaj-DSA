class Solution:
    def removeElement(self, nums, val):
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                # Swap:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i


# Important point:
# I initialized j as j = 1, which missed the case when the first element may be the val.
# So the correct approach is to initialize j as j = 0, which checks the first element too.
