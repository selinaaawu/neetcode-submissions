class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # count frequency of each task
        freq = Counter(tasks)

        # max heap = (count, CPU tasks) for retrieval of most frequent task
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # queue = (idle time, -count) for processing tasks, FIFO
        queue = deque()
        
        time = 0
        while maxHeap or queue:
            # one CPU cycle passed
            time += 1

            # if no elements to process, skip to next timing
            if not maxHeap:
                time = queue[0][0]
            # otherwise, process & decrement count & push to queue
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append((time + n, count))

            # if idle time passed, 
            if queue and queue[0][0] == time:
                heapq.heappush(maxHeap, queue.popleft()[1])

        return time
        