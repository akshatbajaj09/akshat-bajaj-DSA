def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

def solve():
    nums = [0,1,0,3,12]
    print(moveZeroes(nums))

if __name__ == '__main__':
    solve()