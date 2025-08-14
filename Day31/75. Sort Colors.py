# Method - 1:
# Bubble sort:
def sortColors1(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n):
        swap = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                swap = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if swap == False:
            break
    return nums


# Method - 2:
# Insertion sort:
def sortColors2(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


# Method - 3:
# Selection sort:
def sortColors3(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n):
        current_min = i
        for j in range(i, n):
            if nums[j] < nums[current_min]:
                current_min = j
        # swap:
        nums[i], nums[current_min] = nums[current_min], nums[i]
    return nums


# Method - 4:
# Quick sort:
def quickSort(nums, left, right):
    # Base case:
    if left >= right:
        return
    # Recursive case:
    p = partition(nums, left, right)
    quickSort(nums, left, p - 1)
    quickSort(nums, p + 1, right)


def partition(nums, left, right):
    ref = nums[right]
    start = left
    for i in range(left, right + 1):
        if nums[i] <= ref:
            # swap:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
    return start - 1


def sortColors4(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    quickSort(nums, 0, n - 1)
    return nums


# Method - 5:
# Using two pointers:
def sortColors5(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        else:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
    return nums


# Note: We don't increment i after swapping nums[i] and nums[right] because
# the element which comes from right will remain unchecked in that case, however
# as we are scanning the array from left to right, the element coming from the
# left portion is checked already and hence we increment the i pointer after
# swapping nums[i] and nums[left].


# Execution:
def solve():
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors1(nums))
    print(sortColors2(nums))
    print(sortColors3(nums))
    print(sortColors4(nums))
    print(sortColors5(nums))


if __name__ == "__main__":
    solve()
