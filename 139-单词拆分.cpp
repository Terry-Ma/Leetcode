class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> nums(n, false);

        for(int i = n - 1; i > -1; i--){
            for(auto word : wordDict){
                if(i + word.size() <= n && string(s.substr(i, word.size())) == word){
                    if(i + word.size() == n || nums[i + word.size()])
                        nums[i] = true;
                }
            }
        }
        
        return nums[0];
    }
};
