class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> myvector;
        
        dfs(result, myvector, n, k);

        return result;
    }

    void dfs(vector<vector<int>>& result, vector<int>& myvector, int n, int k, int num = 0, int pre = 0){
        if(n - pre < k - num)      // 数量不够，剪枝
            return;
        
        if(num == k){
            result.push_back(myvector);
            return;
        }
        
        for(int i = pre + 1; i < n + 1; i++){
            myvector.push_back(i);
            dfs(result, myvector, n, k, num + 1, i);
            myvector.pop_back();
        }
    }
};
