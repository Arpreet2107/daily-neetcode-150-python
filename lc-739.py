class Solution:
    def dailyTemperatures(self, temperatures):

        # Result list initialized with zeros
        res = [0] * len(temperatures)

        # Stack to store indices of temperatures
        stack = []

        # Iterate through temperature list
        for i, t in enumerate(temperatures):

            # Check if current temperature is warmer
            while stack and t > stack[-1][0]:

                # Pop previous temperature and index
                stackT, stackInd = stack.pop()

                # Calculate number of days waited
                res[stackInd] = i - stackInd

            # Push current temperature and index onto stack
            stack.append((t, i))

        # Return result list
        return res