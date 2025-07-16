# Given a binary array nums, return the maximum number of 
# consecutive 1's in the array.


def find_max_consecutive_ones(nums):
    count = 0
    result = 0
    for i in nums:
        if i == 1:
            count += 1
            result = max(result, count)
        else:
            count = 0
    return result

def solve():
    nums = [1, 1, 0, 1, 1, 1]
    result = find_max_consecutive_ones(nums)
    print("Maximum consecutive 1s are: ", result)

if __name__ == "__main__":
    solve()