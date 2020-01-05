class Solution {
public:
    int numSquares(int n) {
        vector<int> nums = {0, 1};
        for(int i = 0; i < n - 1; i++){
            nums.push_back(INT_MAX);
        }
        
        for(int i = 2; i < n + 1; i++){
            for(int j = 1; j * j <= i; j++){
                nums[i] = min(nums[i], nums[i - j * j] + 1);
            }
        }

        return nums[n];
    }
};
