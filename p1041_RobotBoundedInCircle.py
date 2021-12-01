class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d, x, y = 0, 0, 0
        for c in instructions:
            if c == 'L':
                d = (d - 1) % 4
            elif c == 'R':
                d = (d + 1) % 4
            else:
                x += directions[d][0]
                y += directions[d][1]
        return (d > 0) or (x == 0 and y == 0)
