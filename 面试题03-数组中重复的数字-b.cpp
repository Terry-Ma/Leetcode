class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != i){     // 该位置未就位（排序）
                if(nums[nums[i]] == nums[i])
                    return nums[i];
                else
                    swap(nums[i], nums[nums[i]]);
            }
        }

        return -1;
    }
};
