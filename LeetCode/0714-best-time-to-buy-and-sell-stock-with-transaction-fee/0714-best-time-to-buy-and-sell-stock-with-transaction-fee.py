class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        
        buy_profit = - prices[0]
        sell_profit = 0
        for i in range(1, N):
            buy_profit = max(buy_profit, sell_profit - prices[i])
            sell_profit = max(sell_profit, buy_profit + prices[i] - fee)
        return sell_profit