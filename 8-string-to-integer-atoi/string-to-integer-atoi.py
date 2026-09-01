class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # 2. Determine the sign
        sign = 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1

        elif i < n and s[i] == "+":
            i += 1

        # 3. Build the number
        result = 0

        while i < n and s[i].isdigit():

            digit = ord(s[i]) - ord("0")

            # 4. Check overflow BEFORE multiplying
            if result > (INT_MAX - digit) // 10:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            result = result * 10 + digit

            i += 1

        return sign * result