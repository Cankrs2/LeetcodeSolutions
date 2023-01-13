class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        t = 2
        j = 0
        nums = [1,1]
        while t <= rowIndex:
            for i in range(1,len(nums)):
                nums[j] = nums[j] + nums[i]
                j+=1
            j = 0
            t +=1
            nums.insert(0,1)
                
        return nums
     
        
        
       