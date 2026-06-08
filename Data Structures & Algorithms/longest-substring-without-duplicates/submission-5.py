class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            # duplicate character
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxLength = max(maxLength, len(seen))

        return maxLength
            

        