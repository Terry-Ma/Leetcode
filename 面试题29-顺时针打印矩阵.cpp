class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.empty())
            return vector<int> {};

        int i1 = 0, j1 = 0, i2 = matrix.size() - 1, j2 = matrix[0].size() - 1;
        vector<int> result;

        while(i1 <= i2 && j1 <= j2){
            for(int k = j1; k < j2 + 1; k++){
                result.push_back(matrix[i1][k]);
            }

            for(int k = i1 + 1; k < i2; k++){  
                result.push_back(matrix[k][j2]);
            }

            if(i1 < i2){
                for(int k = j2; k >= i1; k--){
                    result.push_back(matrix[i2][k]);
                }
            }

            if(j1 < j2){
                for(int k = i2 - 1; k > i1; k--){
                    result.push_back(matrix[k][j1]);
                }
            }
            
            i1++;
            j1++;
            i2--;
            j2--;
        }

        return result;
    }
};
