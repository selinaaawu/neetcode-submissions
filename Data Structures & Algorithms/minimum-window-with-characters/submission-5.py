class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ## SLIDING WINDOW | time: O(n + m), space: O(m)
        # want smallest window in s that contains all characters of t
        # valid/window stores {char : count}
        # build valid frequency map for characters in t
        # expand r, add s[r] into window and update matching count if s[r] in valid
        # once window has all required characters -> shrink l until invalid
        # track smallest window so far
        if len(t) > len(s):
            return ""

        # initialize validState
        validState, windowState = {}, {}
        for char in t:
            validState[char] = 1 + validState.get(char, 0)

        have, need = 0, len(validState)
        index, indexLength = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            # add element and update have if EXACT character count matches
            windowState[s[r]] = 1 + windowState.get(s[r], 0)
            if s[r] in validState and windowState[s[r]] == validState[s[r]]:
                have += 1
            
            # if matches, window is valid
            while have == need:
                # update pointers
                if (r - l + 1) < indexLength:
                    index = [l, r]
                    indexLength = r - l + 1
                
                # remove element and update have if character count falls below
                windowState[s[l]] -= 1
                if s[l] in validState and windowState[s[l]] < validState[s[l]]:
                    have -= 1
                l += 1
        
        l, r = index
        return s[l : r + 1] if indexLength != float('inf') else ""
        