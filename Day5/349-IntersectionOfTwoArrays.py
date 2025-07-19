def intersection(nums1, nums2):
    return list((set(nums1)).intersection(set(nums2)))

def solve():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersection(nums1, nums2))

if __name__ == '__main__':
    solve()
