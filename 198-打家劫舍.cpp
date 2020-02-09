class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty())
            return 0;
        
        int num1 = nums[nums.size() - 1], num2 = 0, num;
        for(int i = nums.size() - 2; i > - 1; i--){
            num = num1;
            num1 = max(num1, num2 + nums[i]);
            num2 = num;
        }

        return num1;
    }
};
