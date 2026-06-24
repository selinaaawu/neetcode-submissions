class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # two pointers
        # move right pointer, add char to set for seen
        # move right pointer until char[r] is already seen
        # move left pointer until char[r] is NOT seen
        # keep track of longest length

        l, r = 0, 0
        seen = set()
        maxLength = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, len(seen))
        return maxLength

            


        