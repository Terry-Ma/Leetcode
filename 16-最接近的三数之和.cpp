class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int i, k;
        int j = 1;
        int current = INT_MAX;
        int value;
        
        sort(nums.begin(), nums.end());

        while(j < nums.size() - 1){
            i = 0;
            k = nums.size() - 1;

            while(i < j && j < k){
                value = nums[i] + nums[j] + nums[k];
                if(abs(target - value) < abs(current))
                    current = target - value;
                if(value > target)
                    k -= 1;
                else if(value < target)
                    i += 1;
                else
                    return target - current;
            }

            j += 1;
        }

        return target - current;
    }
};
