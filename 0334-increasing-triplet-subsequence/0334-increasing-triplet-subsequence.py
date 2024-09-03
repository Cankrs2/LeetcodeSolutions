class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        j,k,l = float('inf'),float('inf'),float('inf')
        for i in range(len(nums)):
            if nums[i] < j: j = nums[i]
            elif nums[i] < k and nums[i] != j: k = nums[i] 
            elif nums[i] < l  and (nums[i] != k and nums[i] != j): return True
        return False