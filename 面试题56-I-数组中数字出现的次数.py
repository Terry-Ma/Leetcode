class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        n = 0
        a = 0
        b = 0

        # 求整个nums异或结果
        for i in nums:
            n ^= i
        
        # 求某一位1
        h = 1
        while h & n == 0:
            h <<= 1
        
        # 根据h分为两个子数组，异或得到a，b
        for i in nums:
            if i & h == 0:
                a ^= i
            else:
                b ^= i

        return [a, b]
