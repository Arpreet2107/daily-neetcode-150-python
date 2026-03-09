#leetcode-242. Valid Anagram
from collections import Counter

class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        return Counter(s) == Counter(t)#
        if len (s) != len(t):# If the lengths of the two strings are different, they cannot be anagrams, so we return False
            return False# Create two dictionaries to count the frequency of each character in both strings
        countS,countT = {},{}# Iterate through both strings simultaneously and count the frequency of each character
        for i in range(len(s)):# For each character in the strings, we update the count in the respective dictionary. We use the get method to handle characters that are not yet in the dictionary, defaulting to 0.
            countS[s[i]] = 1 + countS.get(s[i],0)# For each character in the first string, we increment its count in countS. For each character in the second string, we increment its count in countT.
            countT[t[i]] = 1 + countT.get(t[i],0)# After counting the frequency of characters in both strings, we compare the two dictionaries. If they are equal, it means both strings have the same characters with the same frequency, and we return True. Otherwise, we return False.
        for c in countS:# We iterate through the characters in countS and compare their counts with the corresponding counts in countT. If any character has a different count, we return False.
            if countS[c] != countT.get(c,0):# If the count of a character in countS does not match the count of the same character in countT (or if the character is not present in countT), we return False, indicating that the strings are not anagrams.
                return False# If we finish iterating through all characters in countS without finding any discrepancies, it means the strings are anagrams, and we
        return True# return True, indicating that the strings are anagrams.

# Time complexity: O(n) where n is the length of the strings, because we need to count the frequency of each character in both strings.
# Space complexity: O(1) because the number of possible characters is limited (e.g., 26 lowercase letters), so the space used by the dictionaries is constant.
