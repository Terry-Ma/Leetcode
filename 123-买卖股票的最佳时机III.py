class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[[float('-inf'), float('-inf')], [float('-inf'), float('-inf')]] for i in range(len(prices))]
        dp[0][0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0][1] = max(dp[i - 1][0][1], -prices[i])
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][0][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i][0][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])

        return max(0, dp[-1][0][0], dp[-1][1][0])
