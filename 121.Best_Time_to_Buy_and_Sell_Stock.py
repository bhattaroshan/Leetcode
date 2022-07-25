class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn, mx = float('inf'), 0
        for i in range(len(prices)):
            mn = min(mn,prices[i])
            mx = max(mx,prices[i]-mn)
        return mx