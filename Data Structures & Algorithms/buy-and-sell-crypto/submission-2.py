class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        n = len(prices)
        # Time: O(n), Space: O(1)
        l, r = 0, 1 # l = buy, r = sell
        profit = 0
        while l < n and r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
                r += 1
            # move buy to minimum if found
            else:
                l = r
                r += 1
        return max_profit if max_profit > 0 else 0