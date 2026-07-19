"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # min num room to scheduel all meetings without conflict

        ## SWEEP LINE | time: O(), space: O()
        # create line of all events
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        # sort by start time & process -1 before +1
        events.sort(key=lambda x: (x[0], x[1]))
        
        # meeting room needed = max active rooms
        active = 0
        minActive = 0
        for event in events:
            if event[1] == 1:
                active += 1
                minActive = max(minActive, active)
            else:
                active -= 1
        return minActive





        