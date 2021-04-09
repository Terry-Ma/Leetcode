class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> src2dsts(numCourses);
        for(auto edge : prerequisites){
            src2dsts[edge[1]].push_back(edge[0]);
        }
        int src = 0;
        vector<int> path;
        vector<int> node_state(numCourses, 0);
        bool res = true;
        for(int i = 0; i < numCourses; i++){
            if(node_state[i] != 2){
                bool cur_res = dfs(src2dsts, i, path, node_state);
                if(!cur_res){
                    res = false;
                    break;
                }
            }
        }

        int left = 0;
        int right = path.size() - 1;
        while(left < right){
            int tmp = path[right];
            path[right] = path[left];
            path[left] = tmp;
            left++;
            right--;
        }

        return res ? path : vector<int>(0);
    }

    bool dfs(vector<vector<int>>& src2dsts, int src, vector<int>& path, vector<int>& node_state){
        if(node_state[src] == 1)
            return false;

        node_state[src] = 1;
        for(int dst : src2dsts[src]){
            if(node_state[dst] != 2){
                if(!dfs(src2dsts, dst, path, node_state))
                    return false;
            }
        }
        node_state[src] = 2;
        path.push_back(src);

        return true;
    }
};
