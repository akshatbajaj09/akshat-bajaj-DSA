def removeDuplicates(nums):
    left = 2
    for right in range(left, len(nums)):
        if nums[right] != nums[left - 2]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return left


def solve():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = removeDuplicates(nums)
    print("k: ", k)
    print("Output: ", nums[:k])  # Expected: [0, 0, 1, 1, 2, 3, 3]


if __name__ == "__main__":
    solve()
