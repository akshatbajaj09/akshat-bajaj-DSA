class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    x = 1
                    while j + x < len(nums2):
                        if nums2[j + x] > nums2[j]:
                            ans.append(nums2[j + x])
                            break
                        else:
                            x += 1
                    if j + x == len(nums2):
                        ans.append(-1)
        return ans


# The above solution is not optimal.
# The optimal approach will be tried later.
