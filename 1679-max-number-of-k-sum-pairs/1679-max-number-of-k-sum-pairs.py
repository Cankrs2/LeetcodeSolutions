class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = {}
        pairs = 0
        for i in range(len(nums)):
            if nums[i] in dict and dict[nums[i]]  :
                dict[nums[i]]-=1
                pairs+=1
            else:
                val = k - nums[i]
                dict[val] = dict.get(val, 0) + 1
        return pairs