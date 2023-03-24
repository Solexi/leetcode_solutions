class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        int_val = 0
        
        for i in range(len(s)):
            if i > 0 and roman_to_integer[s[i]] > roman_to_integer[s[i-1]]:
                int_val += roman_to_integer[s[i]] - 2 * roman_to_integer[s[i-1]]
            else:
                int_val += roman_to_integer[s[i]]
    
        return int_val