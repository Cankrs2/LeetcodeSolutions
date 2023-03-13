class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            for j in range(i,-1,-1):
                if nums[j] > nums[i]:
                    nums[i] ,nums[j] = nums[j] , nums[i]
                    i = i-1
                elif nums[j] == nums[i]:
                    pass
                else:
                    break
        