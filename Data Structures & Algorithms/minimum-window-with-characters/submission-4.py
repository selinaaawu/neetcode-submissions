class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        left = 0
        right = float('inf')
        minString = ""

        # initialize validState
        validState, windowState = {}, {}
        for char in t:
            validState[char] = 1 + validState.get(char, 0)

        have, need = 0, len(validState)
        # index, indexLength = [-1, -1], 

        l = 0
        for r in range(len(s)):
            # add element and update have if matches
            windowState[s[r]] = 1 + windowState.get(s[r], 0)
            if s[r] in validState and windowState[s[r]] == validState[s[r]]:
                have += 1
            print("add: ", windowState)
            
            # if matched, update pointers
            while have == need:
                if (r - l + 1) < (right - left + 1):
                    left = l
                    right = r
                    minString = s[left:right + 1]
                
                # remove element
                windowState[s[l]] -= 1
                if s[l] in validState and windowState[s[l]] < validState[s[l]]:
                    have -= 1
                l += 1
                print("remove: ", windowState)

        return minString

        

        