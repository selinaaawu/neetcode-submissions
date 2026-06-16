class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # TWO POINTERS | time: O(n), space: O(1)
        # move pointer from smaller bar to maximize area
        max_area = 0

        left, right = 0, len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        