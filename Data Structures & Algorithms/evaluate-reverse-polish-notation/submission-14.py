class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ## STACK | time: O(n), space: O(n)
        # stack bc most recent numbers are the ones used next
        # if num, push onto stack
        # if operator, pop two numbers, apply operation, push result to stack
        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                num2 = stack.pop()
                num1 = stack.pop()

                match token:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(float(num1) / num2))
                        print(stack[-1])
            else:
                stack.append(int(token))
        
        return stack.pop()
        