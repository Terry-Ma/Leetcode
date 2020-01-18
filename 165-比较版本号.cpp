class Solution {
public:
    void split_by_dot(string version, vector<int>& int_vec){
        string cur_str = "";
        for(auto i : version){
            if(i == '.'){
                int_vec.push_back(stoi(cur_str));
                cur_str = "";
            }
            else
                cur_str += i;
        }
        int_vec.push_back(stoi(cur_str));
    }

    int compareVersion(string version1, string version2) {
        vector<int> vec1, vec2;
        split_by_dot(version1, vec1);
        split_by_dot(version2, vec2);
        int v1, v2;

        int i = 0;
        while(i < vec1.size() || i < vec2.size()){
            v1 = i < vec1.size() ? vec1[i] : 0;
            v2 = i < vec2.size() ? vec2[i] : 0;
            if(v1 > v2)
                return 1;
            else if(v1 < v2)
                return -1;
            i ++;
        }
        
        return 0;
    }
};
