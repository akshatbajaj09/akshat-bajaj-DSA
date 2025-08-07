nums = [1, 5, 1, 7, -4, 0]
n = len(nums)
print("Unsorted nums: ", nums)
for i in range(1, n):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
print("Sorted nums: ", nums)
