class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyprice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < minBuyprice:
                minBuyprice = prices[i]
            else:
                profit = max(profit, prices[i] - minBuyprice)

        return profit