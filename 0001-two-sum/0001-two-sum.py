class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len((nums))):
            result = target - nums[i]
            if result in hashmap:
                return i, hashmap[result]
            hashmap[nums[i]] = i 