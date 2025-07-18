def removeElement(nums, val):
    k = 0  
    left = 0  
    for right in range(left, len(nums)):
        if nums[right] != val:
            k += 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1                
    return k

def solve():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    removeElement(nums, val)
    print(nums)

if __name__ == '__main__':
    solve()