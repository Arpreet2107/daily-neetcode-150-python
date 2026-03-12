class Solution:
    def characterReplacement(self, s, k):

        # Dictionary to count frequency of characters in window
        count = {}

        # Left pointer of sliding window
        left = 0

        # Variable to track maximum frequency character in window
        max_freq = 0

        # Result variable for longest valid substring
        result = 0

        # Iterate through string with right pointer
        for right in range(len(s)):

            # Increase frequency of current character
            count[s[right]] = 1 + count.get(s[right], 0)

            # Update max frequency seen in current window
            max_freq = max(max_freq, count[s[right]])

            # Check if replacements needed exceed k
            if (right - left + 1) - max_freq > k:

                # Reduce frequency of left character
                count[s[left]] -= 1

                # Move left pointer to shrink window
                left += 1

            # Update maximum valid substring length
            result = max(result, right - left + 1)

        # Return result
        return result