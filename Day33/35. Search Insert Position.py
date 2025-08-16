def searchInsert(nums, target):
    # Lower Bound:
    n = len(nums)
    l = 0
    r = n - 1
    ans = n
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def solve():
    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))


if __name__ == "__main__":
    solve()
