def getConcatenation(nums):
    ans = nums
    ans.extend(nums)
    return ans


def solve():
    nums = [1, 2, 1]
    print(getConcatenation(nums))


if __name__ == "__main__":
    solve()
