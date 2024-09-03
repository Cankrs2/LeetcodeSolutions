class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        j,k = float('inf'),float('inf')
        for i in nums:
            if i <= j: j = i
            elif i <= k: k = i 
            else: return True
        return False