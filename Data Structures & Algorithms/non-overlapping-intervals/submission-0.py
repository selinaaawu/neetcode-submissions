class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # remove min # intervals to make intervals non-overlapping

        # overlap when start before last end
        # remove largest interval
        # keep interval w earlier end -> more space for future intervals

        intervals.sort(key=lambda x: x[1])

        keep, remove = 0, 0
        lastEnd = float('-inf')
        for start, end in intervals:
            
            # no overlap, starts after last end
            if start >= lastEnd:
                lastEnd = end
            else:
                remove += 1
        
        return(remove)



        
        