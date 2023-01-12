class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)
        while left < right:
            totalTime = 0
            mid = left + (right-left)//2
            for i in range(0, len(piles)):
                if piles[i] % mid == 0:
                    totalTime = piles[i]/mid + totalTime
                else:
                    totalTime = ((piles[i]//mid) +1) + totalTime
            if totalTime <= h:
                right = mid
            else:
                left = mid+1
        return right