def lowerBound(nums, target):
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


def upperBound(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    ans = n
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def searchRange(nums, target):
    lb = lowerBound(nums, target)
    ub = upperBound(nums, target)
    if lb == ub:
        # number is not present in array
        return [-1, -1]
    else:
        return [lb, ub - 1]


def solve():
    nums1 = [5, 7, 7, 8, 8, 9, 10]
    target1 = 9
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    nums3 = []
    target3 = 0
    nums4 = [5, 7, 7, 8, 8, 10]
    target4 = 8
    print(searchRange(nums1, target1))
    print(searchRange(nums2, target2))
    print(searchRange(nums3, target3))
    print(searchRange(nums4, target4))


if __name__ == "__main__":
    solve()
