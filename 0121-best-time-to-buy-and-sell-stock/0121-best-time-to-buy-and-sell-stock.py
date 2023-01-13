class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        min_price = float('inf')
        for i in prices:
            min_price = min(min_price, i)
            maxi = max(maxi, i-min_price)
        return maxi
        
        