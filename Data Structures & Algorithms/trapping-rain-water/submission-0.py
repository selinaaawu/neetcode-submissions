class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft < maxRight: # 0 < 1
                left += 1
                maxLeft = max(height[left], maxLeft)
                maxWater += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                maxWater += maxRight - height[right]
        return maxWater

