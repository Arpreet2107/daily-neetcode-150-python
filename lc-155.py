class MinStack:

    def __init__(self):

        # Main stack to store all values
        self.stack = []

        # Stack to keep track of minimum values
        self.minStack = []

    def push(self, val):

        # Push value to main stack
        self.stack.append(val)

        # Push the minimum value so far to minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):

        # Remove element from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self):

        # Return the top element of main stack
        return self.stack[-1]

    def getMin(self):

        # Return the minimum element in the stack
        return self.minStack[-1]