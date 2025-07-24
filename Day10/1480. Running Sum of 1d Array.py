def runningSum(nums):
    current_sum = 0
    result = []
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result


def solve():
    nums = [1, 2, 3, 4]
    print(runningSum(nums))


if __name__ == "__main__":
    solve()
