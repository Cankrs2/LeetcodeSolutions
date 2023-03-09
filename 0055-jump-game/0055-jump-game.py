class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        
        left,right = 0,0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left,right+1):
                farthest = max(farthest, i+nums[i])
                if farthest >= len(nums)-1:
                    return True
            left = right + 1
            right = farthest
            if left > right:
                return False
        return False