class Solution:
    def evalRPN(self, tokens):

        # Stack to store numbers
        stack = []

        # Iterate through each token
        for c in tokens:

            # If token is "+"
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            # If token is "-"
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            # If token is "*"
            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            # If token is "/"
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                # Convert number string to integer and push to stack
                stack.append(int(c))

        # Final result will be the only element in stack
        return stack[0]