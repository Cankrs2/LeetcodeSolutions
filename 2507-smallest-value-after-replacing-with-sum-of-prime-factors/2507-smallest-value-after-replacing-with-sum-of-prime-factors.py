class Solution:
    def smallestValue(self, n: int) -> int:
        m, s = n, 0
        for i in range(2,n+1):
            while m % i == 0:
                s += i
                m //= i

        return s if s == n else self.smallestValue(s)
