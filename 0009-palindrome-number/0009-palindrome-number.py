class Solution:
    def isPalindrome(self, x: int) -> bool:
        newString = str(x)
        if (newString == newString[::-1]):
            return True
        else:
            return False