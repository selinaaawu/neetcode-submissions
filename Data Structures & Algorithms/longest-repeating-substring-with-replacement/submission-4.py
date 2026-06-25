class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ## SLIDING WINDOW | time: O(n), space: O(1)
        # variable size
        # window is valid IFF window size - max frequency <= k
        # characters that AREN'T the most frequent need to be replaced
        # expand window, update frequency of char and highest char frequency
        # if window validity violated -> adjust count, shrink window

        charMap = defaultdict(int)
        maxLength = 0

        l = maxFrequency = 0
        for r in range(len(s)):
            charMap[s[r]] += 1
            maxFrequency = max(maxFrequency, charMap[s[r]])

            # window size - max frequency > k -> shrink window
            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
            
        