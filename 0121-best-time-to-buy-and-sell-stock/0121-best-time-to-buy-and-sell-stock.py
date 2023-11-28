class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 100000
        max_val = 0
        for i in prices:
            min_val = min(i,min_val)
            max_val = max(max_val , i-min_val)
        return max_val