class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = ''.join(list(reversed(s[i])))
        return " ".join(s)