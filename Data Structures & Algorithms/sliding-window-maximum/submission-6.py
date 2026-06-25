class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ## SLIDING WINDOW w DEQUE | time: O(n), space: O(k)
        # monotonically decreasing deque stores indices of elements
        # front of deque always holds current window's maximum
        # expand r, remove nums < nums[r], add r to deque
        # shrink l if l > d[0] (window too big)
        # when window == size k, record front of deque
        maxElement = []
        d = deque()         # stores indices

        l = 0
        for r in range(len(nums)):
            # maintain decreasing order in deque
            while d and nums[d[-1]] < nums[r]:
                d.pop()

            # add current element
            d.append(r)

            # remove old indices (d[0]) that are out of current window
            while d and d[0] < l:
                d.popleft()
            
            # once window reaches size k, record max
            if r >= k - 1:
                maxElement.append(nums[d[0]])
                l += 1
        
        return maxElement

        ## SLIDING WINDOW w HASH MAP MAX | time: O(nk), space: O(1)
        maxElement = [0] * (len(nums) - k + 1)
        numMap = {}

        for r in range(k):
            numMap[nums[r]] = 1 + numMap.get(nums[r], 0)
        
        l = 0
        for r in range(k, len(nums)):
            maxElement[r - k] = max(numMap)
            print(maxElement)

            # add character
            numMap[nums[r]] = 1 + numMap.get(nums[r], 0)

            # remove character
            numMap[nums[l]] -= 1
        maxElement[len(nums) - k] = max(numMap)
        print(maxElement)
        
        return maxElement
        