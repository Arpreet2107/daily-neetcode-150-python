class Solution:
    def maxArea(self, height):

        # Initialize two pointers
        left = 0
        right = len(height) - 1

        # Variable to store maximum water area
        max_area = 0

        # Loop while pointers do not meet
        while left < right:

            # Calculate width between two lines
            width = right - left

            # Height is determined by the shorter line
            h = min(height[left], height[right])

            # Calculate current area
            area = width * h

            # Update maximum area if current area is larger
            max_area = max(max_area, area)

            # Move the pointer of the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the maximum area found
        return max_area