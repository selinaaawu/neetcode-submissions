class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # return largest rectangle that can be formed

         ## STACK (ONE PASS) | time: O(n), space: O(n)
        # stack stores (index, height) in increasing height order ONLY
        # if new bar shorter than top of stack -> pop and update max area
        # otherwise, add to stack w leftmost index
        # pop remaining bars from stack and update max area

        maxArea = 0
        stack = []
        
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                prevI, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight * (i - prevI))
                start = prevI
            stack.append((start, height))

        # don't forget to process remaining stack elements
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))

        return maxArea

        ## STACK (OPTIMAL) | time: O(1), space: O(1)
        # I DON'T REALLY GET THIS
        # stack stores (index, height) in increasing height order ONLY
        # if shorter bar -> pop as height, width = new top to curr index - 1
        # for loop ensures every bar gets popped
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
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
        