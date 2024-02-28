class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        for i in range(4):
            for c in instructions:
                if c == "G":
                    x, y = x+dx, y+dy
                elif c == "L":
                    dx, dy = -dy, dx
                elif c == "R":
                    dx, dy = dy, -dx
            if x == 0 and y == 0:
                return True
        return False