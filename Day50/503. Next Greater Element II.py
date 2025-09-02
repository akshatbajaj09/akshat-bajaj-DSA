class Solution:
    def nextGreaterElements(self, nums):
        nums += nums
        n = len(nums)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            while len(st) > 0 and st[-1] <= nums[i]:
                st.pop()
            if len(st) == 0:
                ans[i] = -1
            else:
                ans[i] = st[-1]
            st.append(nums[i])
        required_ans = len(ans) // 2
        return ans[:required_ans]
