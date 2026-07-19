"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        ## SORTING | time: O(n log n), space: O(1)
        # meeting overlaps when previous ends after current starts
        
        # sort by start time
        intervals.sort(key=lambda x: x.start)

        # for each interval
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]     # previous interval
            curr = intervals[i]         # current interval

            # if previous ends after current start -> overlap !!
            if prev.end > curr.start:
                return False
        return True
