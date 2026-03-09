class Solution:
    def twoSum(self, nums, target):
        # Create an empty dictionary to store numbers and their indices
        # Format: {number : index}
        num_map = {}

        # Loop through the list using enumerate
        # enumerate gives both index (i) and value (num)
        for i, num in enumerate(nums):

            # Calculate the number needed to reach the target
            complement = target - num

            # Check if the complement already exists in the dictionary
            # If it exists, we have found the two numbers that sum to target
            if complement in num_map:

                # Return the index of the complement and current index
                return [num_map[complement], i]

            # If complement not found, store the current number and index
            num_map[num] = i
        # If we finish the loop without finding a solution, return an empty list
        return []
# Time Complexity
# O(n)
# Space Complexity
# O(n)