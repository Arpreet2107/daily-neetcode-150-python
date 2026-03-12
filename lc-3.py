class Solution:
    def lengthOfLongestSubstring(self, s):

        # Set to store unique characters in current window
        charSet = set()

        # Left pointer of sliding window
        left = 0

        # Variable to store maximum length found
        result = 0

        # Iterate through string with right pointer
        for right in range(len(s)):

            # If duplicate character appears
            while s[right] in charSet:

                # Remove leftmost character from the set
                charSet.remove(s[left])

                # Move left pointer to shrink window
                left += 1

            # Add current character to the set
            charSet.add(s[right])

            # Update maximum substring length
            result = max(result, right - left + 1)

        # Return the longest substring length
        return result