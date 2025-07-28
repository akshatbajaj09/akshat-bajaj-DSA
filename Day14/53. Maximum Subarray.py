def maxSubArray(nums):
    max_sub = nums[0]
    current_sum = 0
    for num in range(len(nums)):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[num]
        max_sub = max(current_sum, max_sub)
    return max_sub


def solve():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))


if __name__ == "__main__":
    solve()
