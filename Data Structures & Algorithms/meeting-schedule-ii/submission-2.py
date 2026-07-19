"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # min num room to schedule all meetings without conflict

        ## TWO POINTERS | time: O(n log n), space: O(n)
        if not intervals:
            return 0

        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        rooms, e = 0, 0
        for s in range(len(start)):
            # meeting ends before another starts -> free room
            if start[s] >= end[e]:
                e += 1
            # meeting starts before another ends -> need new room
            else: 
                rooms += 1
        return rooms


        ## MIN HEAP | time: O(n log n), space: O(n)
        # sort by start time 
        intervals.sort(key=lambda x: x.start)

        # MinHeap stores end times
        minHeap = []
        for interval in intervals:
            # if meeting start time >= earliest end time -> reuse room
            if minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            
            # push current meeting into room
            heapq.heappush(minHeap, interval.end)
        return len(minHeap)


        ## SWEEP LINE | time: O(n log n), space: O(n)
        # create line of all events
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        # sort by start time & process -1 before +1
        events.sort(key=lambda x: (x[0], x[1]))
        
        # meeting room needed = max active rooms
        active = 0              # curr count
        maxActive = 0           # result
        for time, delta in events:
            active += delta
            maxActive = max(maxActive, active)
        return maxActive
        