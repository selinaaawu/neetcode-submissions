class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # return largest rectangle that can be formed
        # [ 7 1 7 2 2 4]
        
        ## STACK
        # for every bar, find how far wide before bumping into shorter bar
        # stack store (index, height)

        maxArea = 0
        stack = []
        
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                prevI, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight * (i - prevI))
                start = prevI
            stack.append((start, height))

        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))

        return maxArea


        ## BRUTE FORCE | time: O(n^2), space: O(11)
        # for every bar, treat as shortest bar in rectangle and find width
        # find max rectangle area found
        n = len(heights) 
        maxArea = 0

        for i, height in enumerate(heights):
            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= heights[i]:
                rightMost += 1 

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= heights[i]:
                leftMost -= 1

            width = (rightMost - 1) - (leftMost + 1) + 1
            maxArea = max(maxArea, height * width)
        return maxArea