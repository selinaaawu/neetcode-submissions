class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countV = {}
        for i in range(len(nums)):
            countV[nums[i]] = 1 + countV.get(nums[i], 0)
            if countV[nums[i]] >= 2:
                return True
        
        return False
        