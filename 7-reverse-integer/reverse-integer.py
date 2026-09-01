class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        limit = 2**31 - 1

        while x:
            x, digit = divmod(x, 10)

            if rev > limit // 10 or (rev == limit // 10 and digit > limit % 10):
                return 0

            rev = rev * 10 + digit

        return sign * rev