class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## STACK | O(N) 
        result = [0] * len(temperatures)
        stack = []                  # [temp, index] pair

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackI = stack.pop()
                result[stackI] = i - stackI
            stack.append((temp, i))

        return result



        ## BRUTE FORCE | O(N^2)
        result = [0] * len(temperatures)
        print(result)

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        print(result)
        return result
    