from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        # Deque will store indices of useful elements
        q = deque()

        # List to store results
        res = []

        # Left pointer of window
        left = 0

        # Iterate through array
        for right in range(len(nums)):

            # Remove smaller elements from back of deque
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index to deque
            q.append(right)

            # Remove leftmost index if it's outside window
            if q[0] < left:
                q.popleft()

            # Once window reaches size k
            if (right + 1) >= k:

                # Front of deque contains index of max element
                res.append(nums[q[0]])

                # Move window forward
                left += 1

        # Return list of maximum values
        return res