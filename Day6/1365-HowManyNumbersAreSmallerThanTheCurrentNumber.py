def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
    return result

def solve():
    nums = [8,1,2,2,3]
    # Expected output = [4,0,1,1,3]
    print(smallerNumbersThanCurrent(nums))

if __name__ == '__main__':
    solve()