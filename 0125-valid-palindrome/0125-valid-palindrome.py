class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        if s == "":
            return True
        for char in s:
            if not char.isalnum():
                continue
            chars.append(char)
        print(chars)
        chars = "".join(str(x).lower() for x in chars)
        reversed_chars = chars[::-1]

        if reversed_chars == chars:
            return True
        return False
        