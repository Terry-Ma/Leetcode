class Solution {
public:
    int numTrees(int n) {

        vector<int> nums = {1, 1};
        
        for(int i = 0; i < n - 1; i++){
            int num = 0;
            for(int j = 0; j < i + 2; j++){
                num += nums[j] * nums[i + 1 - j];
            }
            nums.push_back(num);
        }

        return nums[n];
    }
};
