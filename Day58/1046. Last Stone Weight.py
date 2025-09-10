import heapq


class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            diff = a - b
            if diff != 0:
                heapq.heappush(stones, -diff)
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
