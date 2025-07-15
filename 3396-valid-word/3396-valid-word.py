class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        has_vowels, has_cons = False, False
        if len(word) < 3:
            return False
        for char in word:
            if not (char.isalpha() or char.isdigit()):
                return False
            if char.isdigit():
                continue
            elif char.isalpha():
                if char in vowels:
                    has_vowels = True
                else:
                    has_cons = True
            else:
                return False
        return has_vowels and has_cons