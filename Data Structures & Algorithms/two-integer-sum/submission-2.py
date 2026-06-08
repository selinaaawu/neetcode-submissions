class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find index of # s.t. add up to target #

        # HASH MAP
        # map # to index, check if # in map
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i
        return False

        # BRUTE FORCE | time: O(n^2), space: O(1)
        # check every possible combo
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return False
        