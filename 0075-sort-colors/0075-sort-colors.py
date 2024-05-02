class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        left,right = 0, len(nums)-1
        while i <len(nums):
            if nums[i]==0 and left<=i:
                nums[left],nums[i] = nums[i],nums[left]
                left+=1
                i-=1
            elif nums[i] == 2 and right >= i:
                nums[right], nums[i] = nums[i], nums[right]
                right-=1
                i-=1
            i+=1
        return nums
            

        
        