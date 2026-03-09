#leetcode 49: Group Anagrams
# Example
# Input
# ["eat","tea","tan","ate","nat","bat"]
# Output
# [["eat","tea","ate"],["tan","nat"],["bat"]]
# Time Complexity
# O(n * k log k)
# n = number of words
# k = length of each word
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        # Create a defaultdict where each key maps to a list
        # This will store grouped anagrams
        anagram_map = defaultdict(list)

        # Loop through each word in the input list
        for word in strs:

            # Sort the characters of the word
            # Anagrams will produce the same sorted string
            sorted_word = "".join(sorted(word))

            # Use the sorted word as the key
            # Append the original word to the list
            anagram_map[sorted_word].append(word)

        # Return all grouped anagrams as a list
        return list(anagram_map.values())