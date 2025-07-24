def removeDuplicates(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left


def solve():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    k = removeDuplicates(nums)
    print("k: ", k)
    print("Output: ", nums[:k])


if __name__ == "__main__":
    solve()
