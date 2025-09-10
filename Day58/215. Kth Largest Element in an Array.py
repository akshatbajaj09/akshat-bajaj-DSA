import heapq


class Solution:
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -(heapq.heappop(nums))

    # Method - 2:

    def findKthLargest2(self, nums, k):
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
