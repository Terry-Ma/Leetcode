class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board[i][j] += 1
            for i in range(len(board)):
                for j in range(len(board[0])):
                    alive_cnt = 0
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]) and abs(board[x + i][y + j]) == 2:
                            alive_cnt += 1
                    if alive_cnt <= 1 or alive_cnt >= 4 or (alive_cnt == 2 and abs(board[i][j]) == 1):
                        board[i][j] = -1 * board[i][j]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board[i][j] = 1 if board[i][j] > 0 else 0
