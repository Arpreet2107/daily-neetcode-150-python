class Solution:
    def productExceptSelf(self, nums):
        
        # Get the length of the input list
        n = len(nums)

        # Create a result array initialized with 1s
        # This will store the final products
        res = [1] * n

        # Variable to store prefix product (product of elements before index)
        prefix = 1

        # First pass: compute prefix products
        for i in range(n):
            
            # Store the current prefix product at index i
            res[i] = prefix

            # Update prefix by multiplying current number
            prefix *= nums[i]

        # Variable to store suffix product (product of elements after index)
        suffix = 1

        # Second pass: compute suffix products from right to left
        for i in range(n - 1, -1, -1):

            # Multiply current result value with suffix product
            res[i] *= suffix

            # Update suffix by multiplying current number
            suffix *= nums[i]

        # Return the final result array
        return res