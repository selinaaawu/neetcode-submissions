class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## BINARY SEARCH | O(logn)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

        # ## BRUTE FORCE | O(N)
        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i
        # return -1
        