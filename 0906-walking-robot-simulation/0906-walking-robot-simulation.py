class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # N, E, S, W
        d = 0
        x, y = 0, 0
        out = 0
        obstacle = {tuple(x) for x in obstacles}

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]

                for _ in range(c):
                    if (x + dx, y + dy) in obstacle:
                        break
                    x, y = x + dx, y + dy
                    out = max(out, x**2 + y**2)

        return out
