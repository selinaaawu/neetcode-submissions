class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # MIN-HEAP | time: O(m log k), space: O(k)
        self.k = k
        self.minHeap = nums                 # largest -> min-heap
        heapq.heapify(self.minHeap)         # O(n), turn into min-heap

        # if heap size > k, remove smallest element
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        ## SORTING | time: O(m*nlogn), space: O(m)
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        ## MIN-HEAP | time: O(m log k), space: O(k)
        heapq.heappush(self.minHeap, val) 

        # if size too big, remove smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # smallest elemtn = minHeap[0] contains kth largest number
        return self.minHeap[0]

        ## SORTING | time: O(m*nlogn), space: O(m)
        self.nums.append(val)                       # add value
        self.nums.sort()                            # O(n log n)
        return self.nums[len(self.nums) - self.k]   # kth largest from back        
