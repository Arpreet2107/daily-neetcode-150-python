class Solution:
    def checkInclusion(self, s1, s2):

        # If s1 is longer than s2, permutation is impossible
        if len(s1) > len(s2):
            return False

        # Create frequency arrays for both strings (26 letters)
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Fill initial frequency counts
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Variable to track matches
        matches = 0

        # Count initial matches between both arrays
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Sliding window through s2
        left = 0
        for right in range(len(s1), len(s2)):

            # If all 26 characters match, permutation found
            if matches == 26:
                return True

            # Add new character to window
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1

            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1

            # Remove leftmost character
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1

            left += 1

        # Check final window
        return matches == 26