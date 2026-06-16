class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # TWO POINTERS | time: O(n^2), space: O(1)
        # fix one number, two pointer to search for other two
        # skip all duplicate values
        # if sum > 0, too large, decrement right
        # if sum < 0, too small, increment left
        nums.sort()
        result = []
    
        for i, target in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = target + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1

        return result

        # BRUTE FORCE | time: O(n^3)
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(i) for i in result]



        