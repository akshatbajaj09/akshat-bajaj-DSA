nums = [1, 8, 7, 5]
print("Unsorted nums: ", nums)
n = len(nums)
for i in range(n):
    current_min = i
    for j in range(i + 1, n):
        if nums[j] < nums[current_min]:
            current_min = j

    # swap:
    nums[i], nums[current_min] = nums[current_min], nums[i]
print("Sorted nums: ", nums)
