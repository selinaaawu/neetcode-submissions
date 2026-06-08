class Solution:
    def trap(self, height: List[int]) -> int:
        # final max area of water that can be trapped between bars
        # water level = min(left, right) - curr level

        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        waterLevel = 0

        while left < right:
            if height[left] <= height[right]: 
                left += 1
                maxLeft = max(maxLeft, height[left])
                waterLevel += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                waterLevel += maxRight - height[right]
        return waterLevel






















        totalWater = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            # left is bottleneck
            if maxLeft < maxRight: # 0 < 1
                left += 1
                maxLeft = max(height[left], maxLeft)
                totalWater += maxLeft - height[left]
            # right is bottleneck
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                totalWater += maxRight - height[right]
        return totalWater
