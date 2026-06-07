class MinStack:

    def __init__(self):
        self.stack = []
        # Stores redundant data, but enables O(1) runtime
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        prev = self.min_stack[-1] if len(self.min_stack) else float("inf")
        if self.min_stack == [] or val < prev:
            self.min_stack.append(val)
        else: 
            self.min_stack.append(prev)

    def pop(self) -> None:
        self.stack.pop()
        # min_stack has same size as self.stack so no problem
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
