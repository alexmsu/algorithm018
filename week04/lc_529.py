class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        direction = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
        
        q = deque([(click[0], click[1])])
        while q:
            i, j = q.popleft()
            if board[i][j] == "E":
                neis = [(i + x, j + y) for x, y in direction if 0 <= i + x < len(board) and 0 <= j + y < len(board[0])]
                cnt = sum([board[x][y] == "M" for x, y in neis])
                if cnt == 0:
                    board[i][j] = "B"
                    for x, y in neis:
                        q.append((x, y))
                else:
                    board[i][j] = str(cnt)
                          
        return board