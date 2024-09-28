class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left,right = 0,k-1
        sub_sum = sum(nums[0:k])
        max_average = sub_sum/k
        while right < len(nums)-1:
            sub_sum -= nums[left]
            left+=1
            right+=1
            sub_sum+= nums[right]
            max_average = max(max_average,sub_sum/k)
        
        return max_average