class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ## FOR LOOP GREEDY | time: O(n), sapce: O(n)
        # insert newInterval into intervals s.t. intervals has no overlapping
        result = []
        for i in range(len(intervals)):
            # 1: intervals[i] completely after newInterval
            # -> newInterval[end] before intervals[i][start]
            # no overlap possible, add newInterval & everything after intervals[i]
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # 2: intervals[i] completely before newInterval
            # -> newInterval[start] after intervals[i][end]
            # no overlap possible, append intervals[i] to result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # 3: intervals[i] overlaps with newInterval
            # expand newInterval to cover both ranges
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        return result

        
        ## WHILE LOOP GREEDY | time: O(n), sapce: O(n)
        # insert newInterval into intervals s.t. intervals has no overlapping
        result = []
        i, n = 0, len(intervals)

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
        