class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        heights = [0] * len(matrix[0])
        result = float('-inf')
        
        for i in range(len(matrix)):
            heights = [i * int(j) + int(j) for i, j in zip(heights, matrix[i])] + [-1]
            mystack = [(-1, -1)]
            cur_index = 0

            while not (len(mystack) == 2 and mystack[-1][0] == -1):
                if heights[cur_index] >= mystack[-1][0]:
                    mystack.append((heights[cur_index], cur_index))
                    cur_index += 1

                else:
                    h, i = mystack.pop()
                    result = max(result, h * (cur_index - mystack[-1][1] - 1))

            heights.pop()    # 把末尾加的0去掉
        
        return result
