class Solution:
    def isValid(self, s):

        # Create a stack to store opening brackets
        stack = []

        # Dictionary to map closing brackets to opening brackets
        closeToOpen = {")":"(", "}":"{", "]":"["}

        # Iterate through each character in the string
        for c in s:

            # If the character is a closing bracket
            if c in closeToOpen:

                # Pop from stack if not empty, otherwise use placeholder
                top = stack.pop() if stack else "#"

                # If popped element does not match the expected opening bracket
                if closeToOpen[c] != top:
                    return False

            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)

        # If stack is empty, all brackets matched correctly
        return not stack