class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def count_palindromes(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            # Count odd-length palindromes with s[i] as center
            count_palindromes(i, i)

            # Count even-length palindromes with s[i] and s[i+1] as centers
            count_palindromes(i, i + 1)

        return count