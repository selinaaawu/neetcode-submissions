class Solution:
    def isValid(self, s: str) -> bool:
        paranthesisMap = {"{" : "}", "[" : "]", "(" : ")"}
        stack = []

        for char in s:
            if char in paranthesisMap:
                stack.append(char)
            elif stack and char == paranthesisMap[stack[-1]]:
                stack.pop()
            else:
                return False
        return True if not stack else False

        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.append(char)
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        