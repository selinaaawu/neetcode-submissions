class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ## TWO POINTER w MATCHES | time: O(n + 26), space: O(26)
        # s1 cannot be longer than s1
        if len(s1) > len(s2):
            return False
        
        # define/update states
        validState = [0] * 26
        windowState = [0] * 26
        for i in range(len(s1)):
            validState[ord(s1[i]) - ord('a')] += 1
            windowState[ord(s2[i]) - ord('a')] += 1
        
        # define/update matches
        matches = 0
        for i in range(26):
            matches += 1 if validState[i] == windowState[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            windowState[index] += 1
            if validState[index] == windowState[index]:
                matches += 1
            elif validState[index] + 1 == windowState[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            windowState[index] -= 1
            if validState[index] == windowState[index]:
                matches += 1
            elif validState[index] - 1 == windowState[index]:
                matches -= 1
            
            l += 1
            
        return matches == 26

        ## TWO POINTER w ARRAY | time: O(26n), space: O(26)
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

        if windowState == validState:
            return True
                
        l = 0
        for r in range(windowLength, len(s2)):
            # add right character
            windowState[ord(s2[r]) - ord('a')] += 1

            # remove left character
            windowState[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if windowState == validState:
                return True

        return False

        ## TWO POINTER w DICT | time: O(n * unique char), space: O(unique char)
        # s1 cannot be longer than s2
        if len(s1) > len(s2):
            return False

        validState = Counter(s1)
        validLength = len(s1)

        # initialize window state
        windowState = {}          # {char : count}
        for r in range(validLength):
            windowState[s2[r]] = 1 + windowState.get(s2[r], 0)
        
        if windowState == validState:
            return True
                
        l = 0
        for r in range(validLength, len(s2)):
            # add right character
            windowState[s2[r]] = 1 + windowState.get(s2[r], 0)

            # remove left character
            windowState[s2[l]] -= 1
            if windowState[s2[l]] == 0:
                del(windowState[s2[l]])
            l += 1

            if windowState == validState:
                return True

        return False
        