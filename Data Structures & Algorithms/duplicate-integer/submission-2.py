class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # countV = {}
        # for num in nums:
        #     countV[num] = 1 + countV.get(num, 0)
        #     if countV[num] >= 2:
        #         return True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # return len(nums) != len(set(nums))
        
        
        