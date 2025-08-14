# Counting Sort algorithm:

# Time complexity: O(n + k), where k is the range of data.

# Note: This algorithm can be implemented for negative numbers in the array as
# well, but for now we are doing only for positive numbers. Hence, k can be
# said to be the max of the given array.

# Space complexity: O(k)


def sortArray(nums):
    n = len(nums)
    maximum = max(nums)
    freq_array = [0] * (maximum + 1)
    for num in nums:
        freq_array[num] += 1
    i = 0
    for j in range(len(freq_array)):
        while freq_array[j] > 0:
            nums[i] = j
            i += 1
            freq_array[j] -= 1
    return nums


def solve():
    nums = [5, 2, 3, 1]
    print(sortArray(nums))


if __name__ == "__main__":
    solve()
