class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y = 0, 0
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = 0
        res = 0
        obstaclesSet = set(map(tuple, obstacles))
        
        for c in commands:
            if c == -2: d = (d - 1) % 4
            elif c == -1: d = (d + 1) % 4
            else:
                for _ in range(c):
                    if (x + direction[d][0], y + direction[d][1]) not in obstaclesSet:
                        x += direction[d][0]
                        y += direction[d][1]
                        res = max(res, x * x + y * y)
                    
        return res