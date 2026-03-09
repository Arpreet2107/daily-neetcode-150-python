#leetcode-217  
class Solution:
    def containsDuplicate(seld,nums:List[int]) -> bool:
        hashset = set()# Create an empty set to store unique numbers
        for num in nums:# Iterate through each number in the input list
            if num in hashset:# Check if the number is already in the set
                return True# If it is, we have found a duplicate, so we return True
            hashset.add(num)# If the number is not in the set, we add it to the set for future reference
        return False# If we finish iterating through the list without finding any duplicates, we return False
# Time complexity: O(n) due to the set lookup and insertion operations, which on average are O(1) but can be O(n) in the worst case.
# However, since we are only doing a single pass through the list, the overall time complexity is O(n).
# Space complexity: O(n)