class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ## count the number of concurrent 1's or 0's
        occurrence = []
        res = 0
        for i in range(len(s)):
            if s[i - 1] == s[i]:
                if occurrence == []:
                    occurrence.append(0)
                occurrence[-1]+=1
            else:
                occurrence.append(1)
        print(occurrence)
        ## count the substrings
        for i in range (1, len(occurrence)):
            res += min(occurrence[i-1], occurrence[i])
        return res
        