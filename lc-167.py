class Solution:
    def twoSum(self, numbers, target):

        # Initialize two pointers
        # left starts at the beginning of the array
        left = 0

        # right starts at the end of the array
        right = len(numbers) - 1

        # Continue looping while left pointer is less than right pointer
        while left < right:

            # Calculate the sum of elements at both pointers
            current_sum = numbers[left] + numbers[right]

            # If the sum equals the target
            if current_sum == target:

                # Return the indices (1-indexed as required by the problem)
                return [left + 1, right + 1]

            # If the sum is smaller than target
            elif current_sum < target:

                # Move the left pointer to the right to increase the sum
                left += 1

            # If the sum is greater than target
            else:

                # Move the right pointer to the left to decrease the sum
                right -= 1