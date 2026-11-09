class MinStack:
    # stack stores value
    # minstack store min value sofar
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        minSoFar = min(self.minStack[-1] if self.minStack else val, val)
        self.minStack.append(minSoFar)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
