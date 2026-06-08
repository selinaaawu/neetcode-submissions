class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:


            if token in "+-*/":
                b, a = numStack.pop(), numStack.pop()
                equation = a + token + b
                numStack.append(str(int(eval(equation))))
                print(numStack)
            else:
                numStack.append(token)
        return int(numStack.pop())

        