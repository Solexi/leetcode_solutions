class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        return -1
        