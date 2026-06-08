class Solution:
    def isValid(self, s: str) -> bool:
        paranthesisMap = {"{" : "}", "[" : "]", "(" : ")"}
        stack = []

        for char in s:
            if char in paranthesisMap.keys():
                stack.append(char)
            elif stack and char == paranthesisMap[stack[-1]]:
                stack.pop()
            else:
                return False
        return True if not stack else False
        