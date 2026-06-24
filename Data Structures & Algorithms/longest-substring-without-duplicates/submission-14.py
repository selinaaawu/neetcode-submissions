class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ## SLIDING WINDOW W HASH MAP | time: O(n), space: O(1)
        # hash map stores {char : index}
        # expand window by moving right pointer
        # if repeated character, set left to latest index + 1 OR l (not backward)
        charMap = {}
        maxLength = 0

        l = 0
        for r in range(len(s)):
            if s[r] in charMap:
                l = max(charMap[s[r]] + 1, l)
            charMap[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
        return maxLength

        ## SLIDING WINDOW W HASH SET | time: O(n), space: O(1)
        # set to store seen elements
        # expand window by moving right pointer 
        # if repeated character, shrink window until duplicate is removed
        # keep track of longest length

        seen = set()
        maxLength = 0

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength
        