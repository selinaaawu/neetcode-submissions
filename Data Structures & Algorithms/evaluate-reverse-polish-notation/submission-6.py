class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if token in "+-*/":
                b, a = numStack.pop(), numStack.pop()
                if token == "+":
                    numStack.append(a + b)
                elif token == "-":
                    numStack.append(a - b)
                elif token == "*":
                    numStack.append(a * b)
                elif token == "/":
                    numStack.append(int(a / b))
            else:
                numStack.append(int(token))
        return numStack.pop()

        