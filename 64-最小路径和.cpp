class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> myvector(n, grid[m - 1][n - 1]);
        for(int i = n - 2; i > -1; i--){
            myvector[i] = grid[m - 1][i] + myvector[i + 1];
        }

        for(int i = m - 2; i > -1; i--){
            myvector[n - 1] += grid[i][n - 1];
            for(int j = n - 2; j > -1; j--){
                myvector[j] = grid[i][j] + min(myvector[j + 1], myvector[j]);
            }
        }

        return myvector[0];
    }
};
