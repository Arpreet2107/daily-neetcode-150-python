from collections import Counter

class Solution:
    def minWindow(self, s, t):

        # Edge case
        if t == "":
            return ""

        # Count characters needed from string t
        countT = Counter(t)

        # Dictionary to track window character counts
        window = {}

        # Number of characters currently matched
        have = 0

        # Total unique characters needed
        need = len(countT)

        # Result variables (length, left, right)
        res = [-1, -1]
        resLen = float("inf")

        # Left pointer
        left = 0

        # Expand window with right pointer
        for right in range(len(s)):

            c = s[right]

            # Add character to window count
            window[c] = 1 + window.get(c, 0)

            # Check if required character frequency met
            if c in countT and window[c] == countT[c]:
                have += 1

            # Try shrinking window when valid
            while have == need:

                # Update minimum window result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Remove left character from window
                window[s[left]] -= 1

                # If requirement breaks, decrease have
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                # Move left pointer
                left += 1

        # Extract substring using stored indices
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""