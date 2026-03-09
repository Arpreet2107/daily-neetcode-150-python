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
# Space complexity: O(n) in the worst case, if all numbers in the input list are unique, we will store all of them in the set.
# Therefore, the space complexity is O(n).

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()# Sort the input list in place
        for i in range(1, len(nums)):# Iterate through the sorted list starting from the second element
            if nums[i] == nums[i - 1]:# Compare each element with the previous one
                return True# If we find two adjacent elements that are the same, we have found a duplicate, so we return True
        return False# If we finish iterating through the list without finding any duplicates, we return False
# Time complexity: O(n log n) due to the sorting step, which dominates the overall time complexity. The subsequent iteration through the sorted list is O(n).
# Space complexity: O(1) if we ignore the space used by the sorting algorithm (which is typically O(log n) for in-place sorting algorithms like Timsort used in Python). 
# If we consider the space used by the sorting algorithm, then the space complexity would be O(log n).