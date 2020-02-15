class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            possible = prices[i] - min_price
            if possible > max_profit:
                max_profit = possible
            if possible < 0:
                min_price = prices[i]
        return max_profit
