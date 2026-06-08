class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        if not nums:
            return 0

        i = 0 
        abs_longest = 1
        curr_longest = 1
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            if nums[i + 1] - nums[i] == 1:
                curr_longest += 1
            else:
                curr_longest = 1
            abs_longest = max(abs_longest, curr_longest)
            i += 1
        return abs_longest



        