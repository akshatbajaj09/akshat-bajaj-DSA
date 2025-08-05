def majorityElement(nums):
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


def solve():
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))


if __name__ == "__main__":
    solve()
