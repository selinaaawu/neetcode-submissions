class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            difference = stone2 - stone1
            if difference != 0:
                heapq.heappush(maxHeap, -difference)
            print(maxHeap)

        return -heapq.heappop(maxHeap) if maxHeap else 0
        