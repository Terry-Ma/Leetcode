class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        result = []
        mylist = []
        mydict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def dfs(s, left, right):
            if left == right:
                result.append(''.join(mylist))
                return
            else:
                for i in mydict[s[left]]:
                    mylist.append(i)
                    dfs(s, left + 1, right)
                    mylist.pop()
        
        dfs(digits, 0, len(digits))

        return result
