def sortArrayByParity(nums):
    left, right = 0, 0
    for right in range(len(nums)):
        if nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


def solve():
    nums = [3, 1, 2, 4]
    print(sortArrayByParity(nums))


if __name__ == "__main__":
    solve()
