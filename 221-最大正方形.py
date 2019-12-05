class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        else:
            mylist = list(map(int, matrix[len(matrix) - 1]))
            max_edge = max(mylist)
            for i in range(len(matrix) - 2, -1, -1):
                for j in range(len(matrix[0]) - 1, -1, -1):
                    if j == len(matrix[0]) - 1:
                        t1 = mylist[j]
                        mylist[j] = int(matrix[i][j])
                    else:
                        t2 = mylist[j]
                        if matrix[i][j] == '0':
                            mylist[j] = 0
                        else:
                            mylist[j] = min(t1, t2, mylist[j + 1]) + 1
                        t1 = t2
                max_edge = max(max_edge, max(mylist))    
            return max_edge ** 2
