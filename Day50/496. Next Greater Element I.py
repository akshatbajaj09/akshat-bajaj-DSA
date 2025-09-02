class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        ans = {}
        st = []
        for i in range(n - 1, -1, -1):
            while len(st) > 0 and st[-1] <= nums2[i]:
                st.pop()
            if len(st) == 0:
                ans[nums2[i]] = -1
            else:
                ans[nums2[i]] = st[-1]
            st.append(nums2[i])

        res = []

        for i in nums1:
            res.append(ans[i])

        return res

        # Or we can also use map function to return res without writing a loop.
        # return list(map(lambda x: ans[x], nums1))
