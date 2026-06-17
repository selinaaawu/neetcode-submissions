class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack stores temp and index
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prevI, prevTemp = stack.pop()
                result[prevI] = i - prevI
            stack.append((i, temp))
        return result
        