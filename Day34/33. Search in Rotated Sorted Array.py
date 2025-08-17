def search(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        # Left sorted portion:
        if nums[l] <= nums[mid]:
            if target > nums[mid]:
                l = mid + 1
            if target < nums[mid]:
                if target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        # Right sorted portion:
        else:
            if target > nums[mid]:
                if target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r = mid - 1
    return -1


def solve():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search(nums, target))


if __name__ == "__main__":
    solve()
