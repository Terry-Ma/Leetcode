class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        dp = [[[float('-inf'), float('-inf')] for i in range(k)] for j in range(len(prices))]
        dp[0][0][1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(k):
                dp[i][j][1] = max(dp[i - 1][j][1], -prices[i] if j == 0 else dp[i - 1][j - 1][0] - prices[i])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])

        return max(0, max([dp[-1][i][0] for i in range(k)]))
