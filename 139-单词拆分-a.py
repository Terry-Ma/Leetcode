class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## 超时写法，但是想记录一下
        ## 这个写法是dfs + 回溯，但是由于没有需要记录的状态
        ## 所以实际上这就是个普通的递归 or 分治
        ## 自上而下导致了大量重复，这也是为什么要使用动态规划
        ## 之前dfs + 回溯之所以不能用动态规划，是因为各种状态不同导致子问题不存在重复
        def dfs(s, index):
            if index == len(s):
                return True
            for subs in wordDict:
                n = len(subs)
                if len(s) - index >= n and s[index:index + n] == subs:    ## 这里要注意index out of range
                    if dfs(s, index + n):
                        return True
            return False
        
        return dfs(s, 0)
