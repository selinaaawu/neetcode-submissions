class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # PREFIX AND SUFFIX
        product = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            product[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]
        
        return product



        # BRUTE FORCE
        product = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                product[i] *= nums[j]
        return product
        