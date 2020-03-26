class Solution:
    def sumNums(self, n: int) -> int:
        def get_sum(n):
            return n and n + get_sum(n - 1)
        
        return get_sum(n)
