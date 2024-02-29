class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            start = s.rfind('(')
            end = s.find(')', start)
            inner_content = s[start+1:end]
            reversed_inner = inner_content[::-1]
            s = s[:start] + reversed_inner + s[end+1:]
        return s