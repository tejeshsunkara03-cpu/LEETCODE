class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):

            odd_length = expand(i, i)

            even_length = expand(i, i + 1)

            length = max(odd_length, even_length)

            if length > end - start + 1:

                start = i - (length - 1) // 2

                end = i + length // 2

        return s[start:end + 1]