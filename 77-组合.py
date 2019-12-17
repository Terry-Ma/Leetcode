class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        mylist = []
        myset = set()

        def dfs(num=0, pre=0):
            if n - pre < k - num:             ## 数字数量不够，剪枝
                return

            if num == k:
                result.append(mylist[:])
                return
            
            for i in range(pre + 1, n + 1):     ## 为避免重复，序列保持有序，后面的比pre大  
                mylist.append(i)
                dfs(num + 1, i)
                mylist.pop()
        
        dfs()

        return result
