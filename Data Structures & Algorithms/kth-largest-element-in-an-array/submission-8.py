class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ## MIN HEAP (OPTIMAL) | time: O(n log k), space: O(k)
        return heapq.nlargest(k, nums)[-1]

        ## MIN HEAP | time: O(n log k), space: O(k)
        # size k MinHeap of largest elements so far
        # root is kth largest element
        minHeap = []
        for num in nums:
            # push element into heap
            heapq.heappush(minHeap, num)

            # if heap size > k: remove smallest element
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]

        # ## SORTING | time: O(n log n), space: O(n)
        return sorted(nums)[len(nums) - k]
        