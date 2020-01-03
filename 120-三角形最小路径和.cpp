class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> nums = triangle[n - 1];

        for(int i = n - 2; i > -1; i--){
            for(int j = 0; j < i + 1; j++){
                nums[j] = triangle[i][j] + min(nums[j], nums[j + 1]);
            }
        }

        return nums[0];
    }
};
