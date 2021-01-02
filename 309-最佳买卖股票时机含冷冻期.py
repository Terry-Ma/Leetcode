class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_arr = [0] * (n + 2)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    dp_arr[i] = max(dp_arr[i], prices[j] - prices[i] + dp_arr[j + 2])
            dp_arr[i] = max(dp_arr[i], dp_arr[i + 1])

        return dp_arr[0]
