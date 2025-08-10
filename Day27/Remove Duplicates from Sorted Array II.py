def removeDuplicates(nums):
    left, right = 0, 0
    while right < len(nums):
        count = 1
        while right + 1 < len(nums) and nums[right] == nums[right + 1]:
            count += 1
            right += 1
        for i in range(min(2, count)):
            nums[left] = nums[right]
            left += 1
        right += 1
    return left


def solve():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = removeDuplicates(nums)
    print("k: ", k)
    print("Output: ", nums[:k])  # Expected: [0, 0, 1, 1, 2, 3, 3]


if __name__ == "__main__":
    solve()
