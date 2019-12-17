class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> myvector;                // 当前排列
        unordered_map<int, int> mymap;          // 当前行列情况，列:行
        for(int i = 0; i < n; i++){
            mymap[i] = -1;
        }
        unordered_set<int> set_add;             // 当前已有行列和
        unordered_set<int> set_minus;           // 当前已有行列差

        dfs(0, n, result, myvector, mymap, set_add, set_minus);

        return result;
    }

    void dfs(int num, int& n, vector<vector<string>>& result, vector<string>& myvector, unordered_map<int, int>& mymap, unordered_set<int>& set_add, unordered_set<int>& set_minus){
        if(num == n){
            result.push_back(myvector);
            return;
        }

        for(int i = 0; i < n; i++){
            if(mymap[i] == -1 && set_add.find(num + i) == set_add.end() && set_minus.find(num - i) == set_minus.end()){
                mymap[i] = num;
                set_add.insert(num + i);
                set_minus.insert(num - i);
                myvector.push_back(string(i, '.') + 'Q' + string(n - i - 1, '.'));
                dfs(num + 1, n, result, myvector, mymap, set_add, set_minus);
                mymap[i] = -1;
                set_add.erase(num + i);
                set_minus.erase(num - i);
                myvector.pop_back();
            }
        }
    }
};
