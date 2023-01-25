class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                number, digit = divmod(number,10)
                total += digit**2
            return total
        slow = n
        fast = get_next(n)
        while slow !=fast and fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
        