class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[float('-inf')] * 3 for i in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[-1][0], dp[-1][2])
