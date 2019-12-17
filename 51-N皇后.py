class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        mylist = []
        mydict = {i:-1 for i in range(n)}
        set_add = set()
        set_minus = set()

        def dfs(num = 0):
            if num == n:
                result.append(mylist[:])
                return
            
            for i in range(n):
                if mydict[i] == -1 and num - i not in set_minus and num + i not in set_add:    ## 不冲突
                    mydict[i] = num
                    set_minus.add(num - i)
                    set_add.add(num + i)
                    mylist.append('.' * i + 'Q' + '.' * (n - i - 1))
                    dfs(num + 1)
                    mydict[i] = -1
                    set_minus.remove(num - i)
                    set_add.remove(num + i)
                    mylist.pop()

        dfs()

        return result
