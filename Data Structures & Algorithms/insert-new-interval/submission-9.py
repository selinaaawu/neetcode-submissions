class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # insert newInterval into intervals s.t. intervals has no overlapping intervals
        result = []
        i, n = 0, len(intervals)

        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # intervals[i] completely before newInterval, no overlap
        # intervals[i][end] < newInterval[start]
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # overlap & merge when intervals[i][start] <= newInterval[end]
        # expand newInterval to cover both ranges
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)

        # intervals[i] completely after newInterval, no overlap
        # newInterval[end] < intervals[i][start]
        while i < n:
            result.append(intervals[i])
            i += 1
        return result


        
        