class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## STACK: 
        # stack stores (index, temp)
        # if current temp > top of stack, warmer day found, compute difference in days
        # otherwise add (index, temp) to stack
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prevI, prevTemp = stack.pop()
                result[prevI] = i - prevI
            stack.append((i, temp))
        return result

        ## BRUTE FORCE | time: O(n^2), space: O(n)
        # compare current day with every future day until warmer day or end reached
        # if warmer day, record how many days inbetween, else 0
        # requires scanning same days multipe times
        n = len(temperatures)
        result = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            result.append(count)
        return result

        