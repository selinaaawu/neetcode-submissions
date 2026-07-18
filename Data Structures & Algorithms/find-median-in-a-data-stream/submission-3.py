class MedianFinder:

    def __init__(self):
        self.large = []       # MinHeap stores larger half of #s 
        self.small = []       # MaxHeap stores smaller half of #s
        

    def addNum(self, num: int) -> None:
        # if num greater than smallest # in large -> add to large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        # default: add to small
        else:
            heapq.heappush(self.small, -num)

        # move smaller # to large heap
        if len(self.small) > len(self.large) + 1:
            smaller = -heapq.heappop(self.small)
            heapq.heappush(self.large, smaller)
        # move large # to smaller heap
        if len(self.large) > len(self.small) + 1:
            larger = heapq.heappop(self.large)
            heapq.heappush(self.small, -larger)
                    

    def findMedian(self) -> float:
        # median in small, return negative top
        if len(self.small) > len(self.large):
            return -self.small[0]
        # median in large, return top
        elif len(self.small) < len(self.large):
            return self.large[0]
        # equal length, take average of two #s
        else:
            return (self.large[0] - self.small[0]) / 2.0 
        