def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m - 1, n - 1, m + n - 1
    # i -> end of the elements of nums1 or m - 1.
    # j -> end of nums2 which is n - 1 or len(nums2) - 1.
    # k -> end of nums1 which is (m + n - 1) or len(nums) - 1.
    while j >= 0:
        if i < 0 or nums2[j] > nums1[i]:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        else:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1


def solve():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == "__main__":
    solve()

# Note: We are using 2 pointers i and j and writing using k backwards because we
# are adding bigger elements while sorting and hence we will go from end to start of
# the array. We will also keep an eye on the index out of bounds condition and hence
# add an i < 0 check for it.
