class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        n = len(prices)
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1,n):
                sell = prices[j]
                max_diff = max(max_diff,sell-buy)
        return max_diff
