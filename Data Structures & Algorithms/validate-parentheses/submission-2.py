class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s: 
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            
            elif char == "]":
                if not (len(stack) and stack.pop() == "["):
                    return False
            elif char == ")":
                if not (len(stack) and stack.pop() == "("):
                    return False
            elif char == "}":
                if not (len(stack) and stack.pop() == "{"):
                    return False
        
        return len(stack) == 0
