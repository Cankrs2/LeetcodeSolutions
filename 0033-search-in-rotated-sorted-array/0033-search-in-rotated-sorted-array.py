class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                mid = left
                break
                
        if nums[left] == target:
            return left
        
        if target > nums[len(nums)-1]:
            left,right=0,mid
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                     left = mid+1
                        
        else:
            left,right=mid,len(nums) -1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                    left = mid+1
                
        return -1          
                
