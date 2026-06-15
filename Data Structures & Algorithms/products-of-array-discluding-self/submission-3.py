class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # PREFIX & SUFFIX | time: O(n), space: O(n)
        result = [1] * len(nums)

        # first pass: fill result with prefix product
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # second pass: fill result with postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result 

        # BRUTE FORCE | time: O(n^2), space: O(n)
        # two for loop to iterate through array, skip if self
        result = [1] * len(nums)
        
        j = 0
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            result[i] = product
        return result
        