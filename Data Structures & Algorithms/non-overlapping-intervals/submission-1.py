class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        ## GREEDY | time: O(n log n), space: O(n)
        # remove min # intervals so remaining intervals do not overlap
        # keep interval w earlier end time -> more space for future intervals

        # sort by end time
        intervals.sort(key=lambda x: x[1])

        remove = 0                  # num intervals removed
        lastEnd = intervals[0][1]   # end of first interval
        for start, end in intervals[1:]:
            # starts after last end -> no overlap, update lastEnd
            if start >= lastEnd:
                lastEnd = end
            # interval overlaps with previous -> remove interval
            else:
                remove += 1
        return remove        
        