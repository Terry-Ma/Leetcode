class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j, bound_zero_set):
            bound_zero_set.add((i, j))
            for next_i, next_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (next_i, next_j) not in bound_zero_set and 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) and board[next_i][next_j] == 'O':
                    dfs(board, next_i, next_j, bound_zero_set)

        if len(board) > 2 and len(board[0]) > 2:
            bound_zero_set = set()
            for j in range(len(board[0])):
                if board[0][j] == 'O':
                    dfs(board, 0, j, bound_zero_set)
                if board[-1][j] == 'O':
                    dfs(board, len(board) - 1, j, bound_zero_set)
            for i in range(1, len(board) - 1):
                if board[i][0] == 'O':
                    dfs(board, i, 0, bound_zero_set)
                if board[i][-1] == 'O':
                    dfs(board, i, len(board[0]) - 1, bound_zero_set)
            for i in range(0, len(board)):
                for j in range(0, len(board[0]) - 1):
                    if board[i][j] == 'O' and (i, j) not in bound_zero_set:
                        board[i][j] = 'X'
