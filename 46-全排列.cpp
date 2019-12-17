class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if(nums.empty())
            return vector<vector<int>> {};
        
        unordered_set<int> myset;
        vector<int> myvector;
        vector<vector<int>> result;
        
        helper(nums, myset, myvector, result);

        return result;
    }

    void helper(vector<int>& nums, unordered_set<int>& myset, vector<int>& myvector, vector<vector<int>>& result){
        if(myset.size() == nums.size()){
            vector<int> a(myvector);
            result.push_back(a);
            return;
        }

        for(int i = 0; i < nums.size(); i++){
            if(myset.find(i) == myset.end()){
                myset.insert(i);
                myvector.push_back(nums[i]);
                helper(nums, myset, myvector, result);
                myset.erase(i);
                myvector.pop_back();
            }
        }
    }
};
