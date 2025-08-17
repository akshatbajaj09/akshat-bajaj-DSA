def peakIndexInMountainArray(nums):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        ans = mid
        if mid == 0 or nums[mid] > nums[mid - 1]:
            l = mid + 1
            if nums[l] < nums[mid]:
                break
        else:
            r = mid - 1
    return ans


# Method - 2:
def peakIndexInMountainArray2(nums):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            ans = mid
            r = mid - 1
    return ans


def solve():
    nums = [0, 10, 5, 2]
    print(peakIndexInMountainArray(nums))
    print(peakIndexInMountainArray2(nums))


if __name__ == "__main__":
    solve()
