class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            myset = set()
            for j in i:
                if j != '.':
                    if j in myset:
                        return False
                    myset.add(j)
        
        for j in range(9):
            myset = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in myset:
                        return False
                    myset.add(board[i][j])
        
        for i in range(3):
            for j in range(3):
                myset = set()
                for x in range(3 * i, 3 * (i + 1)):
                    for y in range(3 * j, 3 * (j + 1)):
                        if board[x][y] != '.':
                            if board[x][y] in myset:
                                return False
                            myset.add(board[x][y])

        return True
