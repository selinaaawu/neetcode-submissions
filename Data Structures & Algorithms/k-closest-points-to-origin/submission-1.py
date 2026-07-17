class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ## MAX HEAP | time: O(n log k), space: O(k)
        # size k MaxHeap of closest/smallest distances to (0, 0)
        maxHeap = []        
        for i, point in enumerate(points):
            # calculate distance from origin
            x, y = point
            distance = x ** 2 + y ** 2

            # insert (distance, index of point) to heap
            heapq.heappush(maxHeap, (-distance, i))
            # if heap size > k: remove element w max distance
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        # maxHeap contains k closest points
        result = []
        for distance, i in maxHeap:
            result.append(points[i])
        return result
        