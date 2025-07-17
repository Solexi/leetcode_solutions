class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = "".join(x.lower() for x in s if x.isalnum())
        reversed_chars = s[::-1]
        print(s)

        if reversed_chars == s:
            return True
        return False
        