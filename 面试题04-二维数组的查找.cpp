class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if(matrix.empty())
            return false;
        
        int i = 0, j = matrix[0].size() - 1;
        while(i < matrix.size() & j >= 0){
            if(matrix[i][j] < target)
                i++;
            else if(matrix[i][j] > target)
                j--;
            else
                return true;
        }

        return false;
    }
};
