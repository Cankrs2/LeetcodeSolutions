class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        j = 0
        while j < len(arr): 
            for i in range(len(arr)):
                if (arr[j] == arr[i] * 2 or arr[i] == arr[j] * 2) and i != j:
                    return True
            j = j +1
        return False    