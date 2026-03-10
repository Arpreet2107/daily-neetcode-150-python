class Solution:
    def longestConsecutive(self, nums):

        # Convert list to a set for O(1) lookup
        num_set = set(nums)

        # Variable to track the longest sequence
        longest = 0

        # Iterate through each number
        for n in num_set:

            # Check if n is the start of a sequence
            if (n - 1) not in num_set:

                # Start counting sequence length
                length = 1

                # Check next consecutive numbers
                while (n + length) in num_set:
                    length += 1

                # Update longest sequence length
                longest = max(longest, length)

        # Return the longest consecutive sequence
        return longest