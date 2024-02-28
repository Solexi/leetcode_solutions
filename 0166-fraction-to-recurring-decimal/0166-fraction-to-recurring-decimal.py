class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num = numerator
        denom = denominator
        res = []
        if num == 0:
            return "0"
        if (num < 0) ^ (denom < 0):
            res.append('-')
        num, denom = abs(num), abs(denom)
        res.append(str(num//denom))
        rep_rem = {}
        rem = num % denom

        if rem == 0:
            return ''.join(res)
        res.append(".")
        
        while rem != 0:
            if rem in rep_rem:
                start = rep_rem[rem]
                end = len(res)
                non_repeating_part = ''.join(res[:start])
                repeating_part = ''.join(res[start:end])
                return f"{non_repeating_part}({repeating_part})"
            rep_rem[rem] = len(res)
            rem *= 10
            res.append(str(rem//denom))
            rem %= denom
        return ''.join(res)