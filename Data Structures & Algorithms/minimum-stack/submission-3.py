class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        ## TWO STACKS | time: O(1), space: O(n)
        # minStack stores min value UP TO index
        # min of entire stack will be minStack[-1]
        self.stack.append(val)
        minValue = min(self.minStack[-1] if self.minStack else val, val)
        self.minStack.append(minValue)

        ## BRUTE FORCE
        # self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        ## TWO STACKS
        return self.minStack[-1]

        ## BRUTE FORCE | time: O(n), space: O(n)
        # pop elements to new list and track min element
        # pop elements from new list back to original list
        temp = []
        minNum = self.stack[-1]

        while len(self.stack):
            minNum = min(minNum, self.stack[-1])
            temp.append(self.stack.pop())

        while len(temp):
            self.stack.append(temp.pop())

        return minNum
        
