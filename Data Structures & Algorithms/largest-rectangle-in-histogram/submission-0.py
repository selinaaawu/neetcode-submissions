class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                prevI, prevHeight = stack.pop()
                prevArea = (i - prevI) * prevHeight
                maxArea = max(maxArea, prevArea)
                start = prevI
            stack.append((start, height))

        while stack:
            i, height = stack.pop()
            area = (len(heights) - i) * height
            maxArea = max(maxArea, area)
        return maxArea