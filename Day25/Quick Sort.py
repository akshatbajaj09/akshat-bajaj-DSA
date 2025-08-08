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
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start += 1
    return start - 1


def sortArray(nums):
    quickSort(nums, 0, len(nums) - 1)
    return nums


def solve():
    nums = [5, 1, 1, 2, 0, 0]
    print(sortArray(nums))


if __name__ == "__main__":
    solve()
