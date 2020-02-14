class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def get_sum(i, j):
            s = 0
            while i > 0:
                s += i % 10
                i = i // 10
            while j > 0:
                s += j % 10
                j = j // 10
            return s
        
        def judge(i, j):
            return 0 <= i < m and 0 <= j < n and get_sum(i, j) <= k and (i, j) not in myset
        
        def dfs(i, j):
            myset.add((i, j))
            
            for i, j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if judge(i, j):
                    dfs(i, j)

        myset = set()
        dfs(0, 0)

        return len(myset)
