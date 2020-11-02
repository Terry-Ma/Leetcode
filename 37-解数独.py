class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col, board, row_mat, col_mat, block_mat):
            if row == 9:
                return True
            if col == 8:
                next_row = row + 1
                next_col = 0
            else:
                next_row = row
                next_col = col + 1
            if board[row][col] == '.':
                for value in range(1, 10):
                    if not row_mat[row][value - 1] and not col_mat[col][value - 1] and not block_mat[row // 3][col // 3][value - 1]:
                        row_mat[row][value - 1] = True
                        col_mat[col][value - 1] = True
                        block_mat[row // 3][col // 3][value - 1] = True
                        board[row][col] = str(value)
                        result = dfs(next_row, next_col, board, row_mat, col_mat, block_mat)
                        if result:
                            return True
                        board[row][col] = '.'
                        row_mat[row][value - 1] = False
                        col_mat[col][value - 1] = False
                        block_mat[row // 3][col // 3][value - 1] = False
            else:
                result = dfs(next_row, next_col, board, row_mat, col_mat, block_mat)
                return result

        row_mat = [[False] * 9 for i in range(9)]
        col_mat = [[False] * 9 for i in range(9)]
        block_mat = [[[False] * 9 for i in range(3)] for j in range(3)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    index = int(board[row][col]) - 1
                    row_mat[row][index] = True
                    col_mat[col][index] = True
                    block_mat[row // 3][col // 3][index] = True
        dfs(0, 0, board, row_mat, col_mat, block_mat)
