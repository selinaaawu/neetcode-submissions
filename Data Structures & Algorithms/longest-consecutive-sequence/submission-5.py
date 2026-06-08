class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # HASH SET
        num_set = set(nums)
        longest = 0

        for num in nums:
            # check if start of sequence
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest



        # SORTING
        nums.sort()
        
        if not nums:
            return 0

        abs_longest = 1
        curr_longest = 1
        i = 0 
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
        return max(abs_longest, curr_longest)



        