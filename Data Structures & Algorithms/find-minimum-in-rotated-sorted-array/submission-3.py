class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated sorted array, find minimum element
        # check if mid element is rotated or not rotated
        # if rotated, mid > r, check right side, l = m + 1
        # if not rotated mid < r, check left side, r = m
        # return l

        # [ 1 2 3 4 5 6 ]
        # [ 2 3 4 5 6 1 ]
        # [ 3 4 5 6 1 2 ]
        #       *           5 > 2, part of rotated, search right, l = m + 1
        #       [   *   ]   1 < 2, part of not rotated, search left, r = m
        #       [ *   ]     6 > 1, part of rotated, search right l = m + 1
        # [ 4 5 6 1 2 3 ]
        # [ 5 6 1 2 3 4 ]
        # [   *   ]
        # [ 6 1 2 3 4 5 ]
        #       *
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            print(mid, nums[mid])
            # if not rotated, mid <= rightmost element
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
        