class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        start = 0
        end = 0
        max_length = 0

        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            else:
                char_set.remove(s[start])
                start += 1       
        return max_length