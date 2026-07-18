class MedianFinder:

    def __init__(self):
        self.large = []       # stores larger half of #s 
        self.small = []       # stores smaller half of #s
        

    def addNum(self, num: int) -> None:
        # if num greater than smallest # in large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if abs(len(self.small) - len(self.large)) > 1:
            # move smaller # to large #
            if len(self.small) > len(self.large):
                smaller = -heapq.heappop(self.small)
                heapq.heappush(self.large, smaller)
            else:
                larger = heapq.heappop(self.large)
                heapq.heappush(self.small, -larger)
                
            # remove biggest small number
            
        

    def findMedian(self) -> float:
        print(self.small)
        print(self.large)

        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) / 2.0 
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
        