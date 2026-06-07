class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = None
        stack = []

        for t in tokens:
            if not (t == "+" or t == "-" or t == "/" or t == "*"):
                stack.append(int(t))
            else: 
                op2 = stack.pop()
                op1 = stack.pop()
                
                res = op1+op2 if t == "+" else op1-op2 if t == "-" else op1*op2 if t == "*" else int(op1/op2)
                stack.append(res)

        return stack.pop() 