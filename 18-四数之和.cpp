class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if(nums.size() < 4)
            return vector<vector<int>> {};

        vector<vector<int>> result;
        int t1 = 0, t2, t3, t4, value;
        sort(nums.begin(), nums.end());

        while(t1 < nums.size() - 3){
            t2 = t1 + 1;

            while(t2 < nums.size() - 2){
                t3 = t2 + 1;
                t4 = nums.size() - 1;

                while(t3 < t4){
                    value = nums[t1] + nums[t2] + nums[t3] + nums[t4];

                    if(value == target){
                        result.push_back(vector<int> {nums[t1], nums[t2], nums[t3], nums[t4]});
                        while(nums[++t3] == nums[t3 - 1] && nums[--t4] == nums[t4 + 1] && t3 < t4);
                    }
                    
                    else if(value > target)
                        t4 -= 1;
                    
                    else
                        t3 += 1;
                }

                while(nums[++t2] == nums[t2 - 1] && t2 < nums.size() - 2);

            }

            while(nums[++t1] == nums[t1 - 1] && t1 < nums.size() - 3);

        }

        return result;
    }
};
