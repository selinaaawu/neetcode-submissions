class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # merge overlapping intervals
        # return array of non-overlapping intervals that cover all intervals

        ## SORTING | time: O(n log n), space: O(n)
        # sort by start time
        intervals.sort(key=lambda x: x[0])

        result = []
        for start, end in intervals:
            # if result is empty OR no overlap -> add new interval
            # no overlap when curr start after last end
            if not result or start > result[-1][1]:
                result.append([start, end])
            # overlap -> merge with last interval
            else:
                result[-1][1] = max(result[-1][1], end)
        return result

        ## SWEEP LINE | time: O(n log n), space: O(n)
        events = []
        for start, end in intervals:
            events.append((start, 1))       # start event
            events.append((end, -1))        # end event
        
        # sort by time, process +1 before -1
        events.sort(key=lambda x: (x[0], -x[1]))

        result = []             # store final answer
        active = 0              # event counts
        merged_start = None     # start of interval

        for time, delta in events:
            # if new beginning, start = time
            if active == 0 and delta == 1:
                merged_start = time
            
            active += delta

            # if new ending, push to result
            if active == 0:
                result.append([merged_start, time])
        return result
        