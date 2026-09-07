class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for c in s:
            old_dp = dp

            dp = (2 * dp - last.get(c, 0)) % MOD

            last[c] = old_dp

        return (dp - 1) % MOD