class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        validState = Counter(s1)
        validLength = len(s1)
        print(validState, "length: ", validLength)

        windowState = {}          # {char : count}
        for r in range(validLength):
            windowState[s2[r]] = 1 + windowState.get(s2[r], 0)
            r += 1
        
        if windowState == validState:
            return True
        print(windowState)
                
        l = 0
        for r in range(validLength, len(s2)):
            windowState[s2[r]] = 1 + windowState.get(s2[r], 0)

            windowState[s2[l]] -= 1
            if windowState[s2[l]] == 0:
                del(windowState[s2[l]])
            l += 1

            print(windowState)
            if windowState == validState:
                return True

        return False
        