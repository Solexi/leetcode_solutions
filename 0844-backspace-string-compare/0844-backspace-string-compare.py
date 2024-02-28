class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(input_str: str) -> str:
            result = []
            for char in input_str:
                if char == '#':
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return ''.join(result)

        return process_string(s) == process_string(t)

        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i] == t[j]:
        #             return True
        #     return False