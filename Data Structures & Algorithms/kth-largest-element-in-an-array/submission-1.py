class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ## HEAP
        # size k MinHeap of largest elements so far
        # root is kth largest element
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)

        return minHeap[0]

        # minHeap = []
        # for num in nums:
        #     heapq.heappush(minHeap, num)
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        # return minheap[0]

        # ## SORTING | time: O(n log n), space: O(n)
        # return sorted(nums)[len(nums) - k]
        