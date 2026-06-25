class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 cannot be longer than s2
        if len(s1) > len(s2):
            return False

        validState = [0] * 26
        windowState = [0] * 26
        windowLength = len(s1)

        # character frequency arrays for s1 and s2
        for i in range(windowLength):
            validState[ord(s1[i]) - ord('a')] += 1
            windowState[ord(s2[i]) - ord('a')] += 1

        print(validState)
        print(windowState)
        if windowState == validState:
            return True
                
        l = 0
        for r in range(windowLength, len(s2)):
            # add right character
            windowState[ord(s2[r]) - ord('a')] += 1

            # remove left character
            windowState[ord(s2[l]) - ord('a')] -= 1
            l += 1

            print(windowState)
            if windowState == validState:
                return True

        return False
        