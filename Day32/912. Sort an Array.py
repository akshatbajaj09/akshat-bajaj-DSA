def sortArray(nums):
    n = len(nums)
    minimum = min(nums)
    maximum = max(nums)
    offset = -1 * minimum
    freq_array = [0] * (maximum - minimum + 1)
    for num in nums:
        freq_array[num + offset] += 1
    i = 0
    for j in range(len(freq_array)):
        while freq_array[j] > 0:
            nums[i] = j - offset
            freq_array[j] -= 1
            i += 1
    return nums


def solve():
    nums = [-5, 2, -3, 1]
    print(sortArray(nums))


if __name__ == "__main__":
    solve()
