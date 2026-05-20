class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2  # Represents ways to reach (i-2) and (i-1)
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
