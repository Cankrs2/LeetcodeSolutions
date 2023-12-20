class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result,count = 0,0
        for i in nums:
            if count == 0 or result == i:
                result = i
                count +=1
            else:
                count -=1
        return result