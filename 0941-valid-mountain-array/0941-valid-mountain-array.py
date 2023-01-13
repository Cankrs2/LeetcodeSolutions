class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        j = 0 
        i = len(arr) - 1
        while j< len(arr)-1 and arr[j+1] > arr[j]:
            j += 1
        while arr[i-1] > arr[i] and i!= 1:
            i -= 1
        if j == i and i != len(arr)-1:
            return True
        
            