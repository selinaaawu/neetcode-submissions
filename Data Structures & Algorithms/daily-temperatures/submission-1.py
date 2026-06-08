class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## STACK | O(N) 
        result = [0] * len(temperatures)

        # monotonic decreasing stack
        stack = []
        index = []

        for i, temp in enumerate(temperatures):
            print (i, temp)
            # temperature greater than top of stack
            if stack and temp > stack[-1]:
                while stack and temp > stack[-1]:
                    result[index[-1]] = i - index[-1]
                    stack.pop()
                    index.pop()
                    print(result)
            # temperature less than top of stack
            stack.append(temp)
            index.append(i)

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
    