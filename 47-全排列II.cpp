class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        if(nums.empty())
            return vector<vector<int>> {};
        
        vector<vector<int>> result;
        vector<int> myvector;
        unordered_map<int, int> nums_map;
        for(auto i : nums){
            if(nums_map.find(i) == nums_map.end())
                nums_map[i] = 1;
            else
                nums_map[i] += 1;
        }

        helper(0, nums.size(), result, myvector, nums_map);

        return result;
    }

    void helper(int num, int size, vector<vector<int>>& result, vector<int>& myvector, unordered_map<int, int>& nums_map){
        if(num == size){
            result.push_back(myvector);   
            return;
        }

        for(unordered_map<int, int>::iterator i = nums_map.begin(); i != nums_map.end(); i++){  // 双向迭代器，不是随机访问，只能用!=
            if(i->second > 0){                 // 也可以用auto i : nums_map遍历，后面i.first，i.second
                i->second -= 1;
                myvector.push_back(i->first);
                helper(num + 1, size, result, myvector, nums_map);
                i->second += 1;
                myvector.pop_back();
            }
        }
    }
};
