class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # count frequency of each task
        freq = Counter(tasks)
        print(freq)
        # print(freq.items())
        # print(freq.values())

        # max heap for easy retrieval of most frequent task
        # max heap stores (count, CPU tasks)
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        print(maxHeap)

        # queue for processing tasks, FIFO
        # (time out of queue, count)
        queue = deque()

        minCycle = 0
        while maxHeap or queue:
            # if most recent == current cycle, take 
            while queue and queue[0][0] == minCycle:
                count = queue.popleft()[1]
                heapq.heappush(maxHeap, -count)
            
            count = -heapq.heappop(maxHeap) if maxHeap else 0
            print(minCycle, count)

            if count > 1:
                queue.append((minCycle + n + 1, count - 1))
            print(queue)

            minCycle += 1

        return minCycle
        