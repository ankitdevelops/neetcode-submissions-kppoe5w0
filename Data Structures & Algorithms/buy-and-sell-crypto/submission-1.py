class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_diff = 0
        # n = len(prices)
        # for i in range(n):
        #     buy = prices[i]
        #     for j in range(i + 1,n):
        #         sell = prices[j]
        #         max_diff = max(max_diff,sell-buy)
        # return max_diff

        buy_day = 0
        sell_day = 1
        max_profit = 0
        n= len(prices)
        while sell_day < n:
            if prices[buy_day] <prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit= max(max_profit,profit)
            else:
                buy_day = sell_day
            sell_day += 1
        return max_profit