class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ## SORTING
        return sorted(nums)[len(nums) - k]
        