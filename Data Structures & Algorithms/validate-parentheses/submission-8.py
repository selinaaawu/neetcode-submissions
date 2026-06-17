class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            print(char)
            if char in parentheses_map.values():
                stack.append(char)
            else:
                if stack and stack[-1] == parentheses_map[char]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
        