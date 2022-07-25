class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_negative = False

        if x < 0:
            is_negative = True

        x = abs(x)
        while x > 0:
            m = x % 10
            rev = rev * 10 + m
            x = x // 10

        return rev if not is_negative else rev * (-1)

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
s.reverse(120)
