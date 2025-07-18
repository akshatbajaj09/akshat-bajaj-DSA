def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()

def solve():
    nums1 =[1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    solve()