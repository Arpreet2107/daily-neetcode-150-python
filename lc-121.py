class Solution:
    def maxProfit(self, prices):

        # Variable to store minimum price seen so far
        min_price = prices[0]

        # Variable to store maximum profit
        max_profit = 0

        # Iterate through the price list
        for price in prices:

            # Update minimum price if a smaller price is found
            min_price = min(min_price, price)

            # Calculate potential profit if sold today
            profit = price - min_price

            # Update max profit if this profit is larger
            max_profit = max(max_profit, profit)

        # Return the maximum profit
        return max_profit