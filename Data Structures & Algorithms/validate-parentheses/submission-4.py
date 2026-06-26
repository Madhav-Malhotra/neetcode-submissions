'''
Constraints: 
- Only 6 valid chars
- Return type is boolean (simplifies problem)
- 1000 chars. 

Options: 
- Any opening bracket is added onto the stack
    - Any closing bracket MUST correspond to the opening bracket at TOS
    - Stack must be empty at the end
    - O(n) space complexity and O(n) time complexity
- Optimisation possible: if stack len over n/2, we can stop early
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Init our stack
        stack = []

        for bracket in s:
            # Opening brackets
            if bracket == "[" or bracket == "(" or bracket == "{": 
                stack.append(bracket)
                continue
            
            # Closing brackets (check TOS matches)
            last = stack.pop() if len(stack) else None
            if last is None: 
                return False

            if bracket == "]":  
                if last != "[": 
                    return False
            elif bracket == ")":
                if last != "(": 
                    return False 
            elif bracket == "}":
                if last != "{": 
                    return False

            # Validation 
            else: 
                return False

        # Check stack empty
        return len(stack) == 0