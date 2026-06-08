class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## BINARY SEARCH | O(log n)
        minNum = float('inf')
        left, right = 0, len(nums) - 1
        while left <= right:
            # nums already already sorted -> min at left
            if (nums[left] < nums[right]):
                minNum = min(minNum, nums[left])
                break

            # binary search
            m = left + (right - left) // 2
            minNum = min(minNum, nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else: 
                right = m - 1
        return minNum
                

        ## BRUTE FORCE | O(n)
        return min(nums)
        