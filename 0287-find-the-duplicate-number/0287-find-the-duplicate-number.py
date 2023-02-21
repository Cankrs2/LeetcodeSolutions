class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        secondslow = 0
        while True:
            slow = nums[slow]
            secondslow = nums[secondslow]
            if slow == secondslow:
                return slow