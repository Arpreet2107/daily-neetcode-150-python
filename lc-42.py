class Solution:
    def trap(self, height):

        # Initialize left and right pointers
        left = 0
        right = len(height) - 1

        # Track maximum heights from both sides
        left_max = height[left]
        right_max = height[right]

        # Variable to store total trapped water
        water = 0

        # Continue until pointers meet
        while left < right:

            # If left max is smaller
            if left_max < right_max:

                # Move left pointer
                left += 1

                # Update left max height
                left_max = max(left_max, height[left])

                # Add trapped water at this position
                water += left_max - height[left]

            else:

                # Move right pointer
                right -= 1

                # Update right max height
                right_max = max(right_max, height[right])

                # Add trapped water
                water += right_max - height[right]

        # Return total trapped water
        return water