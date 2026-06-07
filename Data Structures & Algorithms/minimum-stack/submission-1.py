class MinStack:

    def __init__(self):
        self.stack = []
        self.min_el = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_el is None or self.min_el > val: 
            self.min_el = val

    def pop(self) -> None:
        el = self.stack.pop()
        # Happens only occasionally - amortized O(1)
        if el == self.min_el: 
            self.min_el = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_el
        
