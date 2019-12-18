class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        myset = set()         ## 记录用过的格子
        m = len(board)
        n = len(board[0])
        size = len(word)
    
        def dfs(x, y, index):  
            if index == size:
                return True
            
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n and (i, j) not in myset and board[i][j] == word[index]:
                    myset.add((i, j))
                    if dfs(i, j, index + 1):
                        return True
                    myset.remove((i, j))
            
            return False       ## 剪枝
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    myset.add((x, y))
                    if dfs(x, y, 1):
                        return True
                    myset.remove((x, y))

        return False
