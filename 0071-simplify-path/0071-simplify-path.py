class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirNames = path.split('/')
        for name in dirNames:
            if not name or name == ".":
                continue
            if name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(name)
                
        cPath = "/" + "/".join(stack)
        return cPath