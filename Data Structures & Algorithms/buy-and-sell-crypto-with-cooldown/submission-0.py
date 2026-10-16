class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1b, dp1s = 0, 0
        dp2b = 0

        for i in range(n - 1, -1, -1):
            dpb = max(dp1s - prices[i], dp1b)
            dps = max(dp2b + prices[i], dp1s)
            dp2b = dp1b
            dp1b, dp1s = dpb, dps
        
        return dp1b