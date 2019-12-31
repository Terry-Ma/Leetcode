class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size(), j, min_i, min_v;
        
        while(--i > 0){
            if(nums[i - 1] < nums[i])
                break;
        }

        if(i == 0)
            sort(nums.begin(), nums.end());

        else{
            j = i;
            min_v = nums[j];
            min_i = j;

            while(j < nums.size()){
                if(nums[j] < min_v && nums[j] > nums[i - 1]){
                    min_i = j;
                    min_v = nums[j];
                }
                j++;
            }

            swap(nums[i - 1], nums[min_i]);
            sort(nums.begin() + i, nums.end());
        }
    }
};
