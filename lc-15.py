class Solution:
    def threeSum(self, nums):

        # Create a list to store the final triplets
        res = []

        # Sort the array to use two-pointer technique
        nums.sort()

        # Loop through each element as the first number of the triplet
        for i in range(len(nums)):

            # Skip duplicate values to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1

            # Continue until pointers meet
            while left < right:

                # Calculate the sum of the triplet
                total = nums[i] + nums[left] + nums[right]

                # If the sum is greater than 0
                if total > 0:

                    # Move right pointer left to decrease sum
                    right -= 1

                # If the sum is smaller than 0
                elif total < 0:

                    # Move left pointer right to increase sum
                    left += 1

                # If we found a valid triplet
                else:

                    # Add the triplet to result
                    res.append([nums[i], nums[left], nums[right]])

                    # Move left pointer
                    left += 1

                    # Skip duplicate numbers
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        # Return all unique triplets
        return res