class Solution:
    def generateParenthesis(self, n):

        # List to store all valid combinations
        res = []

        # Helper function using backtracking
        def backtrack(openN, closeN, stack):

            # If the number of opening and closing brackets equals n
            if openN == closeN == n:
                res.append("".join(stack))
                return

            # Add opening bracket if we still can
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN, stack)
                stack.pop()

            # Add closing bracket if valid
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1, stack)
                stack.pop()

        # Start recursion
        backtrack(0, 0, [])

        # Return result list
        return res