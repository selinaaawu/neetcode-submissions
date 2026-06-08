class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False








        # countV = {}
        # for num in nums:
        #     countV[num] = 1 + countV.get(num, 0)
        #     if countV[num] >= 2:
        #         return True
        # return False

        # HASH SET
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # HASH SET LENGTH
        # return len(nums) != len(set(nums))
        
        
        