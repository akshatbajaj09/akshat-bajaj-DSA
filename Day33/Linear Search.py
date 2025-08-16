def search(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1


def solve():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))


if __name__ == "__main__":
    solve()
