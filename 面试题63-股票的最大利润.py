class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = prices[0]
        result = 0

        for i in range(1, len(prices)):
            result = max(result, prices[i] - buy)
            buy = min(buy, prices[i])

        return result
