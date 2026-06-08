class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        # initialize pointers at opposite ends of array
        left, right = 0, len(heights) - 1
        while left < right:
            # area = width * height
            area = (right - left) * min(heights[left], heights[right])
            maxWater = max(maxWater, area)

            # move pointer of shorter height inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater
        