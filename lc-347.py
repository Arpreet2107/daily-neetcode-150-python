from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):

        # Count the frequency of each number in the list
        # Example: [1,1,1,2,2,3] -> {1:3, 2:2, 3:1}
        count = Counter(nums)

        # Create buckets where index represents frequency
        # Length is len(nums)+1 because maximum frequency can be n
        freq = [[] for i in range(len(nums) + 1)]

        # Place numbers into buckets based on their frequency
        for num, c in count.items():

            # Append the number to the list at index equal to its frequency
            freq[c].append(num)

        # Create an empty list to store result
        res = []

        # Iterate from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):

            # Loop through numbers in that frequency bucket
            for num in freq[i]:

                # Add the number to the result list
                res.append(num)

                # If we have collected k elements, return the result
                if len(res) == k:
                    return res
# Time Complexity: O(n) to count frequencies and O(n) to place numbers in buckets, resulting in O(n) overall.
# Space Complexity: O(n) for the count dictionary and O(n) for the buckets,