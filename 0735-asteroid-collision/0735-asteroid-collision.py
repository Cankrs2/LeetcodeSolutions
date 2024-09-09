class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i in asteroids:
            while result and i < 0 and result[-1] > 0:
                diff = result[-1] - abs(i)
                if diff > 0:
                    i = 0                    
                elif diff < 0:
                    result.pop()
                else:
                    i = 0
                    result.pop()
            if i != 0: result.append(i)        
            
            
        return result