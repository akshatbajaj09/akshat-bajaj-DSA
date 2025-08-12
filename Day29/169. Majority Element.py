# Method - 1 (Hashing):
def majorityElement1(nums):
    n = len(nums)
    freq_dict = {}
    for num in nums:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
    for num in freq_dict:
        if freq_dict[num] > n / 2:
            return num


# Method - 2 (Recursion):
def major(nums, low, high):
    # Base case:
    if low == high:
        return nums[low]
    # Recursive case:
    mid = (low + high) // 2
    left_major = major(nums, low, mid)
    right_major = major(nums, mid + 1, high)
    if left_major == right_major:
        return left_major
    left = nums[low : mid + 1]
    right = nums[mid + 1 : high + 1]

    if left.count(left_major) > right.count(right_major):
        return left_major
    else:
        return right_major


def majorityElement2(nums):
    return major(nums, 0, len(nums) - 1)


# Method - 3 (The Boyre-Moore algorithm):
def majorityElement3(nums):
    count = 0
    major = nums[0]
    for i in range(len(nums)):
        if count == 0:
            major = nums[i]
        if nums[i] == major:
            count += 1
        else:
            count -= 1
    return major


# Method - 4 (Sorting):
def majorityElement4(nums):
    nums.sort()
    return nums[len(nums) // 2]


# Execution:
def solve():
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement1(nums))
    print(majorityElement2(nums))
    print(majorityElement3(nums))
    print(majorityElement4(nums))


if __name__ == "__main__":
    solve()
