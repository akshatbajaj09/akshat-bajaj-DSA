nums = [1, 7, 8, 4, 5, 1]
print(f"Unsorted nums: ", nums)
n = len(nums)
for i in range(n):
    swap = False
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            swap = True
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    if swap == False:
        break

print(f"Sorted nums: ", nums)

# We can do the same for sorting in descending order by just changing the condition
# from nums[j] > nums[j + 1] to nums[j] < nums[j + 1].
