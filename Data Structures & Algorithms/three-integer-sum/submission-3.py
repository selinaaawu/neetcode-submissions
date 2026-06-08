class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        solution = []
        seen = set()
        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum2 = nums[l] + nums[r]
                if sum2 == target:
                    if tuple([nums[i], nums[l], nums[r]]) not in seen:
                        seen.add((nums[i], nums[l], nums[r]))
                        solution.append([nums[i], nums[l], nums[r]])
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        print(solution)
        return solution

        # for twosum
        # search map for target
        # add target into map
        # if map contains target return index
        # mapping of target -> index
        # add into set()

        # idk
        solutionMap = []
        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                for k in range(r + 1, len(nums)):
                    if nums[l] + nums[r] + nums[k] == 0:
                        # how to get unique ?????
                        solutionMap.append([nums[l], nums[r], nums[k]])
        print (solutionMap)
        return [[0, 0, 0]]


































        output = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            target = -a
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
        return output