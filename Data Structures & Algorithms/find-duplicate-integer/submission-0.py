class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        ## TWO POINTERS: time: O(n), space: O(1)
        # treat array like linked list, value tells you the next index
        # two indices will point to same value, creating cycle
        # use slow & fast pointer to find intersection
        # iterate beginning and meeting point until met again
        # value is duplicate #

        # find intersection point
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find cycle entrance
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return slow


        ## HASH SET | time: O(n), space: O(n)
        duplicate = set()

        for num in nums:
            if num in duplicate:
                return num
            duplicate.add(num)
                
        return -1
        