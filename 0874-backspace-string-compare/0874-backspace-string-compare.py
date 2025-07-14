class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            result = []
            for char in string:
                if char == "#":
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return ''.join(result)
        
        processed_s = process_string(s)
        processed_t = process_string(t)
        
        return processed_s == processed_t
    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     for i in range(len(s)):
    #         if i > 0 and s[i] == "#":
    #             s = s.replace(s[i-1] + s[i], "")
    #             break
    #     for j in range(len(t)):
    #         if j > 0 and t[j] == "#":
    #             t = t.replace(t[j-1] + t[j], "")
    #             break
    #     print(s,t)
    #     if s == t:
    #         return True
    #     else:
    #         return False