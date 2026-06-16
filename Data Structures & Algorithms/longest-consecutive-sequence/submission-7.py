class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return LENGTH of longest consecutive sequence of elements 
        # that can be formed

        # HASH SET | O(n)
        # start counting ONLY if # is beginning of consecutive sequence
        # check if consecutive # exists in set
        seen = set(nums)
        max_length = 0

        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
                max_length = max(max_length, length)
        return max_length

        # SORTING | O(nlogn)
        # sort list so consecutive values are next to each other
        # walk through sorted list and count longest sequence
        # skip if duplicates and reset if new value
        max_length = 0
        nums.sort()
        
        length = 0
        curr = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                length = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            length += 1
            curr += 1
            max_length = max(max_length, length)
        return max_length

        # BRUTE FORCE | O(n^2)
        # convert num to set for O(1) lookups
        # for each num, find longest consecutive sequence of that num
        seen = set(nums)
        max_length = 0

        for num in nums:
            length = 0
            curr = num
            while curr in seen:
                length += 1
                curr += 1
            max_length = max(max_length, length)
        return max_length
