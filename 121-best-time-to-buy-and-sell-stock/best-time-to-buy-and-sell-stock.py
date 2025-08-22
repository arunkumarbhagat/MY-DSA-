class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')   # start with a very high value
        max_profit = 0             # initially no profit

        for price in prices:
            # update the minimum price so far
            if price < min_price:
                min_price = price
            # calculate profit if selling today
            profit = price - min_price
            # update max profit if it's greater
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
