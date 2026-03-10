class Solution:
    def isPalindrome(self, s):

        # Initialize two pointers
        left = 0
        right = len(s) - 1

        # Loop until pointers meet
        while left < right:

            # Skip non-alphanumeric characters on left side
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters on right side
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        # If all characters match, it's a palindrome
        return True